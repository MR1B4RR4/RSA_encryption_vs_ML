# RSA_encryption

The RSA algorithm, named after its inventors Ron Rivest, Adi Shamir, and Leonard Adleman, is a widely used asymmetric cryptographic algorithm for secure communication over insecure channels. Here's a quick description of how it works:

Key Generation:

Choose two distinct prime numbers, p and q.
Compute n = p * q, where n is the modulus for the public and private keys.
Compute φ(n) = (p-1) * (q-1), where φ is Euler's totient function.
Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1 (e is coprime with φ(n)). This e will be the public exponent.
Compute d such that (d * e) % φ(n) = 1. This d will be the private exponent.
Key Distribution:

Public Key: (e, n) is distributed publicly. This is used for encryption.
Private Key: (d, n) is kept secret. This is used for decryption.
Encryption:

To encrypt a message m, where 0 < m < n, compute c = m^e mod n. Here, c is the ciphertext.
Decryption:

To decrypt the ciphertext c, compute m = c^d mod n. Here, m is the original message.
The security of RSA relies on the difficulty of factoring the product of two large prime numbers (n = p * q) into its prime factors. As long as the primes p and q are sufficiently large and chosen randomly, it is computationally infeasible to factorize n and retrieve the private key from the public key. Thus, RSA provides a secure method for encryption and decryption, widely used in various secure communication protocols like SSL/TLS, SSH, and PGP.