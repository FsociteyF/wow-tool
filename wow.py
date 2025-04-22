from ipwhois import IPWhois

def whois_lookup(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print("\n[+] WHOIS Information / معلومات WHOIS:\n")
        for key, value in results.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[!] Error / خطأ: {e}")

if __name__ == "__main__":
    print("=== WOW - WHOIS Lookup Tool ===")
    ip = input("Enter IP address / أدخل عنوان IP: ")
    whois_lookup(ip)
