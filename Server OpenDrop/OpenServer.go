package main
import (
        "fmt"
        "./networking"
        "flag"
        "sync"
) 


// Global variables for flags
var (
    AUTH_PORT string
    SYNC_PORT string
	PROTOCOL string
	)

const(SIZE = 1024
      MAX_USERS = 50
      USERS_PATH = "NUTZERS/"
)

func init(){
	flag.StringVar(&AUTH_PORT, "port", "5000", 
		"auth port")
    flag.StringVar(&SYNC_PORT, "syncport", "5001",
        "sync port") 
	flag.StringVar(&PROTOCOL, "protocol", "tcp",
		"protocol to be used")
}



func main() {
    // WorkGroup
    var wg sync.WaitGroup


    // Getting a server
    fmt.Println("------------------ Welcome to the open server sequence ------------")
    server := networking.GetServer(USERS_PATH, 
        AUTH_PORT, SYNC_PORT, PROTOCOL, MAX_USERS)
    server.Start_services()
    // Moving to a thread the auth service
    fmt.Println("here we go")
    wg.Add(1)
    go server.Run_auth(&wg)
    wg.Wait()
    fmt.Println("All done")


}


