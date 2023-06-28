package main

    import (
        "fmt"
        "log"
        "net/http"
    )

    func handler(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "This is hands-on for dockerizing a golang application")
    }

    func main() {
        http.HandleFunc("/", handler)
        log.Fatal(http.ListenAndServe(":8888", nil))
    }
