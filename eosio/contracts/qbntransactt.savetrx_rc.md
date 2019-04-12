# CONTRACT FOR qbntransactt::savetrx

## ACTION NAME: savetrx

### Parameters
Input parameters:

* `uint64_t id`
* `string type`
* `string sender`
* `string recipient`
* `string status`
* `string sender_currency`
* `string recipient_currency`
* `string sec_transaction_id`
* `double s_request_amount`
* `double r_request_amount`
* `double q_request_amount`
* `double s_amount`
* `double r_amount`
* `double q_amount`
* `string sent_via`
* `string received_via`
* `string sender_ip`
* `string reference`
* `string receipt_no`
* `string metadata`
* `time_point_sec created`
* `time_point_sec updated`


### Intent
INTENT. The intention of the author and the invoker of this contract is to save Transactions relayed to it from the QBN Django API. It shall have no other effect.

### Term
TERM. This Contract expires at the conclusion of code execution.
