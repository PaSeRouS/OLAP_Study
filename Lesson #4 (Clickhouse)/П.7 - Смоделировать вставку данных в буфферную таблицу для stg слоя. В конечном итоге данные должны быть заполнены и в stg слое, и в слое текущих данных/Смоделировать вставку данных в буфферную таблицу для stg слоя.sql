-- Имитация заполнения буферной таблицы
insert into buffer.Shk_LostPost_buff (shk_id, operation_code, dt, lostreason_id) values
(17491557864, 'shkwriteoff', '2024-06-30 19:13:39', 24),
(21195200982, 'shkwriteoff', '2024-06-30 19:13:39', 24),
(18787267451, 'shkfound', '2024-06-30 19:13:35', 0),
(20935096493, 'shkwriteoff', '2024-06-30 19:13:34', 23),
(18777081360, 'shkwriteoff', '2024-06-30 19:13:32', 23),
(20789397223, 'shkfound', '2024-06-30 19:13:24', 0),
(20789397223, 'shkfound', '2024-06-30 19:13:24', 0),
(21769948442, 'shkwriteoff', '2024-06-30 19:13:24', 11),
(13817184128, 'shkfound', '2024-06-30 19:13:23', 0),
(10695279824, 'shkwriteoff', '2024-06-30 19:13:15', 5);


-- Проверяем данные в stg таблице
select *
from stg.Shk_LostPost;


-- Проверяем данные в currently таблице
select *
from currently.Shk_LostPost;