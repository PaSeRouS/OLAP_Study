-- Создание пользователя-админа
create user serov_admin IDENTIFIED with sha256_password by 'serov123';

-- Выдача ролей пользователю-админу
grant current GRANTS on *.* to serov_admin with grant option