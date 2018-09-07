Requirements:
    Installed Docker and Docker Compose.

Actions to run:
    1) Unzip archive activation_portal.zip
    2) docker-compose up

Admin panel:
   http://127.0.0.1:41080/manage

You should change you current admin password in Activation Portal Administrarion board:
    1) Login with admin/admin credentials
    2) Change password in the top right corner.

Available endpoints:
    /codes/*activation_code* 
    
    Activation code is available in admin panel after CEA and CIMA login and password entered (and saved).

Token:
    Access token is located in admin panel (section AUTH TOKEN/Tokens). You can create another user (not admin) and generate access token for him.


Format of generated activation code:
    1) Length of 10 symbols
    2) Contains letters in lowercase
    3) Contanis letters in uppercase
    4) Contains digits






