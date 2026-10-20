# apim-timeout-lab
Purpose: reproduce long-call behaviour on Azure (ACA job -> APIM -> model) to advise a customer. Lab only, no customer data.
Rules:
- Never commit secrets. Config via .env (git-ignored); keep .env.example current.
- Don't deploy or change Azure resources without my explicit OK; show the plan and estimated cost first.
- Label every claim about Azure behaviour "expected" (from docs) or "observed" (from our runs). Cite the Microsoft Learn page for docs claims.
- Small commits, clear messages. Results go in results/ as CSV plus a README table.