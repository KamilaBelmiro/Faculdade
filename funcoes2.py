def loginUsuario(perfil):
    perfil = perfil.lower()
 
    if perfil=="Admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usuário")
        
    loginUsuario("Admin")
    loginUsuario("admin")
    loginUsuario("User")
    loginUsuario("usuário")
    loginUsuario("etc")
    
    
