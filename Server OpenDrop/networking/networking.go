package networking 
import( "io"
    	"log"
    	"net"
    	"time"
    	"math/rand"
    	"fmt"
    	"sync")
// Constants
const(TOKEN_LENGTH = 10
	  BUFFER = 100
	  AUTH = 1
	)


// Basic structures
type user struct{
	name, token string
}

type Server struct {
	// Administrative information
	user_path, auth_port, sync_port, protocol string
	// Current Active users
	active_users []user;
	// 
	server_auth, server_sync net.Listener
	servers_on bool
	lock sync.Mutex
	max_users int
}
// Returns a server object
func GetServer(user_path, auth_port, sync_port, protocol string, max_users int) *Server{
	var OD_server *Server = new(Server);
	OD_server.user_path = user_path
	OD_server.auth_port = auth_port
	OD_server.sync_port = sync_port
	OD_server.protocol = protocol
	OD_server.max_users = max_users
	// Allocating memory for active users list 
	OD_server.active_users = make([]user, 0, max_users)
	return OD_server 
}

func get_token() string{
	rand.Seed( time.Now().UTC().UnixNano())
	var token_bytes []byte= make([]byte, TOKEN_LENGTH)
    for i:=0 ; i<TOKEN_LENGTH ; i++ {
        token_bytes[i] = byte(randInt(65,90))
    }
    return string(token_bytes)
}

func (serv *Server) Start_services() bool{
	serv.servers_on = true
	// Creating listeners
	var (error_auth error
		error_sync error) 

	serv.server_auth, error_auth = net.Listen(serv.protocol, ":"+serv.auth_port)
	serv.server_sync, error_sync = net.Listen(serv.protocol, ":"+serv.sync_port)
	if error_sync != nil || error_auth != nil{
		log.Println(error_auth)
		log.Println(error_sync)
		serv.servers_on = false
		log.Println(serv.protocol)
	}
	return serv.servers_on } 


func (serv *Server) auth_token(conn net.Conn){
	// Gives a token to user
    buffer := make([]byte, BUFFER)
	total_received_bytes := 0
	token := get_token()
	var username string
	inx := -3
    for i:=0;i<AUTH;i++ {
    	fmt.Println(i)
        received_bytes, err := conn.Read(buffer)
        total_received_bytes += received_bytes
        // Error
        if i==0{username = string(buffer)}
        if err != nil {
            if err != io.EOF {
                log.Printf("IO error: %s", err)
            }
            break
        }
    }
    // Data base connection and searching goes here

    // Iterating over array
    // getting lock
    serv.lock.Lock()

	for index, element:= range serv.active_users{
		if element.name == username{
			inx = index
			break
		}
	}
	// Releasing array
	serv.lock.Unlock()

	// If index -3 then user not found adding to the list
	if inx == -3 && len(serv.active_users) == serv.max_users{
		log.Println("Maximum active users reached :(")
		conn.Write([]byte("#NONE"))
		conn.Close()
		return
	}

	// Updating current users
	serv.lock.Lock()

	if inx == -3{
		new_user := user {username, token}
		serv.active_users = append(serv.active_users, new_user)
	}else{
		serv.active_users[inx].token = token
	}
	serv.lock.Unlock()
	information := []byte(token)
	log.Println("Username: ", username, " Token: ", token)
	log.Println("------------>")
	conn.Write(information)
    conn.Close()
    return
}

func (serv *Server) Run_auth(wait *sync.WaitGroup){
	fmt.Println("############### AUTH USERS MODULES ACTIVE #############")
	fmt.Println("Port:"+serv.auth_port)
	for {
		auth_connection, err := serv.server_auth.Accept()
		if err != nil{
			log.Fatal(err)
		}
		// Sending to routine
		go serv.auth_token(auth_connection)
	}
	wait.Done()
}

func randInt(min int , max int) int {
    return min + rand.Intn(max-min)
}

