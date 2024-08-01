create table test.dq_shk_lostpost engine = ReplacingMergeTree order by dt_hour as
select toStartOfHour(dt_operation) dt_hour
     , count() cnt
     , uniq(shk_id) uniq_shk
     , uniq(chrt_id) uniq_chrt
     , countIf(chrt_id, chrt_id < 1 and operation_code = 'shkwriteoff') cnt_0_chrt
     , uniq(create_employee_id) uniq_create_employee
     , countIf(create_employee_id, create_employee_id < 1) cnt_0_create_employee
     , uniq(lostreason_id) uniq_lostreason
     , countIf(lostreason_id, lostreason_id < 1 and operation_code = 'shkwriteoff') cnt_0_lostreason
     , countIf(operation_code, operation_code = 'shkwriteoff') cnt_0_shkwriteoff
     , countIf(lostreason_id, operation_code = 'shkfound') cnt_0_shkfound
     , countIf(lostreason_id, operation_code = '') cnt_0_no_operation_code
from Shk_LostPost
group by dt_hour