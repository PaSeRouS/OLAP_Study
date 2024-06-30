-- Создание пустой таблицы на stg слое
create table if not exists stg.Shk_LostPost
(
    shk_id         Int64,
    dt             DateTime,
    operation_code LowCardinality(String),
    lostreason_id  UInt32
)
engine = MergeTree() ORDER BY shk_id;

-- Создание пустой буферной таблицы
create table if not exists buffer.Shk_LostPost_buff
(
    shk_id         Int64,
    dt             DateTime,
    operation_code LowCardinality(String),
    lostreason_id  UInt32
)
engine = Buffer('stg', 'Shk_LostPost', 16, 10, 100, 10000, 100000, 10000000, 100000000);