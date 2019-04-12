#include <eosiolib/eosio.hpp>
#include <eosiolib/asset.hpp>
#include <eosiolib/time.hpp>
#include <eosiolib/transaction.hpp>
using namespace eosio;
using namespace std;

CONTRACT qbntransactt : public eosio::contract
{

public:
  using contract::contract;

  qbntransactt(eosio::name receiver, eosio::name code, eosio::datastream<const char *> ds) : contract(receiver, code, ds), _balances(receiver, receiver.value), _transactions(receiver, receiver.value) {}

  ACTION initaccnt(uint64_t id, string username, string usertype, double balance, string metadata);

  ACTION deposit(uint64_t id, string username, double amount);

  ACTION savetrx(uint64_t id, string type, string sender, string recipient,
                 string status, string sender_currency, string recipient_currency,
                 string sec_transaction_id, double s_request_amount, double r_request_amount,
                 double q_request_amount, double s_amount, double r_amount, double q_amount,
                 string sent_via, string received_via, string sender_ip, string reference, string receipt_no,
                 string metadata, time_point_sec created, time_point_sec updated);

  // Do not use directly, use the VALIDATE_JSON macro instead!
  void validate_json(
      const string &payload,
      size_t max_size,
      const char *not_object_message,
      const char *over_size_message)
  {
    if (payload.size() <= 0)
      return;

    eosio_assert(payload[0] == '{', not_object_message);
    eosio_assert(payload.size() < max_size, over_size_message);
  }

private:
  TABLE balance
  {
    uint64_t id;
    uint64_t username;
    string usertype;
    double amount = 0.0000;
    string metadata;

    auto primary_key() const { return id; }
    uint64_t by_username() const { return username; }
  };
  typedef eosio::multi_index<"balance"_n, balance, eosio::indexed_by<"username"_n, eosio::const_mem_fun<balance, uint64_t, &balance::by_username>>> balstable;

  TABLE transaction
  {
    uint64_t id;
    string type;
    string sender;
    string recipient;
    string status;
    string sender_currency;
    string recipient_currency;
    string sec_transaction_id;
    double s_request_amount;
    double r_request_amount;
    double q_request_amount;
    double s_amount;
    double r_amount;
    double q_amount;
    string sent_via;
    string received_via;
    string sender_ip;
    string reference;
    string receipt_no;
    string metadata;
    time_point_sec created;
    time_point_sec updated;

    uint64_t primary_key() const { return id; }
  };
  typedef eosio::multi_index<"transaction"_n, transaction> trxtable;

  balstable _balances;
  trxtable _transactions;
};