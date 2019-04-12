#include "qbntransactt.hpp"


#define VALIDATE_JSON(Variable, MAX_SIZE)\
::qbntransactt::validate_json(\
    Variable,\
    MAX_SIZE,\
    #Variable " must be a JSON object (if specified).",\
    #Variable " should be shorter than " #MAX_SIZE " bytes."\
)

ACTION qbntransactt::initaccnt(uint64_t id, string username, string usertype, double balance, string metadata)
{
    // Initializes a new account. Receives from QBN Django.
    eosio_assert(username.size() > 0, "Empty user names not allowed"); // usernames shall not be empty strings
    auto itr = _balances.find(id);
    VALIDATE_JSON(metadata, 32768);
    eosio_assert(itr == _balances.end(), "Hey, looks like this account already exists."); // DO NOT attempt to init an existing account, you.
    _balances.emplace(get_self(), [&](auto &user) {
        user.id = id;
        user.username = name{username}.value;
        user.usertype = usertype;
        user.amount = 0.0000;
        user.metadata = metadata;
    });
}

ACTION qbntransactt::deposit(uint64_t id, string username, double amount)
{
    require_auth(get_self());
    string uname = username;
    eosio_assert(amount > 0.0000, "The amount to deposit should be greater than 0");
    auto itr = _balances.find(id);
    eosio_assert(itr != _balances.end(), "Could not find the user account");
    _balances.modify(*itr, get_self(), [&](auto &user) {
        user.id = id;
        user.username = name{username}.value;
        user.amount = amount;
    });
}

ACTION qbntransactt::savetrx(
    uint64_t id, string type, string sender, string recipient,
    string status, string sender_currency, string recipient_currency,
    string sec_transaction_id, double s_request_amount, double r_request_amount,
    double q_request_amount, double s_amount, double r_amount, double q_amount,
    string sent_via, string received_via, string sender_ip, string reference, string receipt_no,
    string metadata, time_point_sec created, time_point_sec updated)
{
    // eosio_assert(id.size() > 0, "ID must not be empty");
    eosio_assert(type.size() > 0, "type must not be empty");
    eosio_assert(sender.size() > 0, "sender must not be empty");
    eosio_assert(recipient.size() > 0, "recipient must not be empty");
    // CONFIRM ALL FIELDS

    // Save to Table
    auto itr = _transactions.find(id);
    // eosio_assert(itr == _transactions.end(), "looks like this transaction already exist");
    if (itr != _transactions.end())
    {
        // Trx does not exist yet. ADD
        _transactions.emplace(get_self(), [&](auto &trx) {
            trx.id = id;
            trx.type = type;
            trx.sender = sender;
            trx.recipient = recipient;
            trx.status = status;
            trx.sender_currency = sender_currency;
            trx.recipient_currency = recipient_currency;
            trx.sec_transaction_id = sec_transaction_id;
            trx.s_request_amount = s_request_amount;
            trx.r_request_amount = r_request_amount;
            trx.q_request_amount = q_request_amount;
            trx.s_amount = s_amount;
            trx.r_amount = r_amount;
            trx.q_amount = q_amount;
            trx.sent_via = sent_via;
            trx.received_via = received_via;
            trx.sender_ip = sender_ip;
            trx.reference = reference;
            trx.receipt_no = receipt_no;
            trx.metadata = metadata;
            trx.created = created;
            trx.updated = updated;
        });
    }
    else
    {
    }
}
EOSIO_DISPATCH(qbntransactt, (initaccnt)(deposit)(savetrx))