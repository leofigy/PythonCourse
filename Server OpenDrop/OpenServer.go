package main
 
import (
    "io"
    "log"
    "net"
    "time"
    "flag"
)

// Global variables for flags
var (
	Port string
	Protocol string
	)

const(SIZE = 1024)

func init(){
	flag.StringVar(&Port, "port", "5000", 
		"listening port") 
	flag.StringVar(&Protocol, "protocol", "tcp",
		"protocol to be used")
}


func receive_data(conn net.Conn) {
    start := time.Now()
    buffer := make([]byte, SIZE)
    total_received_bytes := 0
    answer := []byte{'r','e','c','e','i','v','e','d','\n'}

    for {
        received_bytes, err := conn.Read(buffer)
        total_received_bytes += received_bytes
        // Error
        if err != nil {
            if err != io.EOF {
                log.Printf("IO error: %s", err)
            }
            break
        }
        log.Printf("---> %s \n (%d bytes)", string(buffer), received_bytes)
        conn.Write(answer)

    }
    log.Printf("%d bytes read in %s", total_received_bytes, time.Now().Sub(start))
    log.Println(" <------ User left")
    conn.Close()
}

func main() {
	flag.Parse()
    server, err := net.Listen(Protocol, ":"+Port)
    if err != nil {
        log.Fatal(err)
    }
    log.Println("############## REMOTE SERVER #################")
    log.Println("Listening on localhost:",Port)
    for {
        connection, err := server.Accept()
        if err != nil {
            log.Fatal(err)
        }
        go receive_data(connection) // This moves connection to a goroutine (light thread)
    }
}


