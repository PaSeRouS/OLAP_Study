-- Создание пустой таблицы на currently слое
create table if not exists currently.Shk_LostPost
(
    shk_id         Int64,
    dt             DateTime,
    operation_code LowCardinality(String),
    lostreason_id  UInt32
)
engine = MergeTree() ORDER BY shk_id;

-- Создание материализованного представления
create materialized view stg.Shk_LostPost_currently to currently.Shk_LostPost as
select shk_id, dt, operation_code, lostreason_id
from stg.Shk_LostPost;
