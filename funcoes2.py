def loginUsuario(perfil):
    perfil = perfil.lower()
 
    if perfil=="Admin":
        print("Bem-vindo, Administrador")
    else:
        print("Bem-vindo, Usu�rio")
        
    loginUsuario("Admin")
    loginUsuario("admin")
    loginUsuario("User")
    loginUsuario("usu�rio")
    loginUsuario("etc")
    
    
