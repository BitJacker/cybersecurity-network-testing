import dns.resolver

domain = input("Dominio: ")
queries = int(input("Numero query: "))

resolver = dns.resolver.Resolver()

for i in range(queries):
    try:
        resolver.resolve(domain, "A")
        print(f"{i+1}: OK")
    except:
        print(f"{i+1}: FAIL")

