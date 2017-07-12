test API for checking if the word is palindrome.

       get string_id value from JSON request for checking
       Example for curl client:
       $ curl -XPOST -d '{"string_id": "test"}'   -H "Content-Type:application/json"   http://127.0.0.1:8888
       few parameters like:
       $ curl -XPOST -d '{"string_id": "ooppoo", "string2_id": "test"}'   -H "Content-Type:application/json"   http://127.0.0.1:8888
