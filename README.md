# What is Cryptography and the History of Cryptography

- Encryption is the process of making data or communication content unreadable by encrypting it. In this process, encryption algorithms are used, which are difficult to understand, and it is ensured that the information becomes understandable only by authorized users. It is used for purposes such as encryption, privacy, security and data integrity.

- The history of cryptography goes back quite a long way. Humans have been using various techniques for thousands of years to transmit and encrypt secret messages. In ancient Egypt, some methods were used to encrypt written messages. During the ancient Greek and Roman periods, encryption became more complex.

- But the basics of modern cryptography, 20. it was laid down at the beginning of the century. Many important encryption algorithms and cryptographic protocols were developed during this period. Especially II. During World War II, advanced cryptographic methods were used to encrypt the military communications of various countries.

- Since the mid-1960s, with the development of public-key cryptography and other modern cryptographic systems, cryptography has undergone a significant transformation. With the spread of the Internet, cryptography has become even more important and has become a basic component used for the security of online communications.

- In recent years, there has been rapid progress in the field of cryptography. With the popularity of technologies such as blockchain and cryptocurrencies, cryptography has had a wider range of uses. Today, cryptography plays an important role in areas such as communication security, data privacy and digital signatures.

# Encryoted_Example

- In this example I have made, we see how an encrypted file is sent.
# How it works, for example:

1-) The crypto key is generated` 'Fernet.a random key is generated using the generate_key() function.

2-) `encrypt_and_write_exception' function: This function encrypts the received exception information and writes it to a log file named `log_file`. Exception information, `cipher_suite.it is encrypted with the encrypt function and saved to the `encrypted_exception` variable. Then, the encrypted exception is added to the log file.

3-) `send_encrypted_email' function: This function performs the process of sending encrypted e-mail. The necessary parameters of the function are the sender's e-mail address (`sender_email`), sender's e-mail password (`sender_password`), the recipient's e-mail address (`receiver_email`), the e-mail subject (`subject`) and the message content (`message`).

   - Encryption operation: `message' variable` 'cipher_suite.it is encrypted using the encrypt function and saved to the `encrypted_message` variable.

   - E-mail creation: An e-mail message is created using the `MimeMultipart` and `MIMEText` classes. the sender, recipient, subject and encrypted message are added to the `msg' object.

   - Sending e-mail: Connecting to the e-mail server using the `smtplib` module (`server.starttls()` and `server.login()`), sending encrypted e-mail (`server.sendmail()`) and terminating the connection (`server.quit()`).

4-) Use case: An example is being created within the main code block. Here, the line `x = 10 / 0` is used to generate an error. Then, the resulting exception (`ZeroDivisionError`) is encrypted with the `encrypt_and_write_exception' function and written to the log file. At the same time, the encrypted error message is sent encrypted with the `send_encrypted_email` function.

In this example, a scenario is simulated in which the exception information is encrypted and saved to a log file when an error occurs, and at the same time an encrypted e-mail is sent. In this way, errors can be tracked and shared in an encrypted way.
