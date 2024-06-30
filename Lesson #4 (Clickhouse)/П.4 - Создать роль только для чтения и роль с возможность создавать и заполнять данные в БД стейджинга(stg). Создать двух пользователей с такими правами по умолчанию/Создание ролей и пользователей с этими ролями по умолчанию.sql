-- Создание роли только для чтения + добавление соответствующих прав
create role readonly;

grant select on *.* to readonly;

-- Создание пользователя с ролью только для чтения по умолчанию
create user if not exists serov_readonly IDENTIFIED with sha256_password by 'readonly123' default role readonly;

-- Создание роли только для чтения + добавление соответствующих прав
create role create_and_insert;

grant create on stg.* to create_and_insert;
grant insert on stg.* to create_and_insert;

-- Создание пользователя с ролью только для чтения по умолчанию
create user if not exists serov_create_and_insert IDENTIFIED with sha256_password by 'creins123' default role create_and_insert;
