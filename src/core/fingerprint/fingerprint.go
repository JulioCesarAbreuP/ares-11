package fingerprint

import (
    "fmt"
    "net"
    "time"
)

// Asset representa un activo descubierto en la red
type Asset struct {
    IP        string    `json:"ip"`
    Port      int       `json:"port"`
    Service   string    `json:"service"`
    Timestamp time.Time `json:"timestamp"`
}

// ScanPort intenta conectar a un puerto TCP y determina si está abierto o cerrado
func ScanPort(ip string, port int) Asset {
    address := fmt.Sprintf("%s:%d", ip, port)
    conn, err := net.DialTimeout("tcp", address, 500*time.Millisecond)

    if err != nil {
        return Asset{
            IP:        ip,
            Port:      port,
            Service:   "closed",
            Timestamp: time.Now(),
        }
    }

    conn.Close()
    return Asset{
        IP:        ip,
        Port:      port,
        Service:   "open",
        Timestamp: time.Now(),
    }
}

// FingerprintHost escanea un conjunto de puertos relevantes para IG1/IG2/IG3
func FingerprintHost(ip string) []Asset {
    ports := []int{
        22,   // SSH
        80,   // HTTP
        443,  // HTTPS
        445,  // SMB
        3389, // RDP
    }

    var results []Asset

    for _, port := range ports {
        results = append(results, ScanPort(ip, port))
    }

    return results
}
