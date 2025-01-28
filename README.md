# SeldeanCrypt

SeldeanCrypt is a lightweight and user-friendly encryption tool designed to secure individual files with ease. Whether you're safeguarding personal photos, sensitive documents, or any other file type, SeldeanCrypt ensures your data remains protected with strong encryption.

## Download

Get the latest version of SeldeanCrypt from the official website:  
[Download SeldeanCrypt](https://sertanbalta.com/Downloads/SeldeanCrypt)

## Usage

### Generating an Encryption Key
To generate a new encryption key, use the following command:

```bash
SeldeanCrypt -o {OUTPUT_KEY_FILE} generate-key
```

**Example:**
```bash
SeldeanCrypt -o MY_KEY.KEYFILE generate-key
```

### Encrypting a File
To encrypt a file, use the following command structure:

```bash
SeldeanCrypt -i {INPUT_FILE} -o {OUTPUT_FILE} -k {KEY_FILE} encrypt
```

**Example:**
```bash
SeldeanCrypt -i FamilyPhoto.png -o EncryptedFile.file -k MY_KEY.KEYFILE encrypt
```

### Decrypting a File
To decrypt a file, use the following command structure:

```bash
SeldeanCrypt -i {INPUT_FILE} -o {OUTPUT_FILE} -k {KEY_FILE} decrypt
```

**Example:**
```bash
SeldeanCrypt -i EncryptedFile.file -o DecryptedPhoto.png -k MY_KEY.KEYFILE decrypt
```

### Key Management

#### Viewing the Key
You can view the contents of your key file using the `cat` command:

```bash
cat MY_KEY.KEYFILE
```

#### Sharing the Key
The key is a plaintext file, making it easy to share. Here’s how to recreate the key file:

1. **Using `echo`:**
   ```bash
   echo "{YOUR_KEY}" > NEW_KEY.KEYFILE
   ```

2. **Using `touch` and `echo`:**
   ```bash
   touch NEW_KEY.KEYFILE
   echo "{YOUR_KEY}" > NEW_KEY.KEYFILE
   ```

Alternatively, you can share the `.KEYFILE` directly.

### Encrypting Multiple Files
To encrypt multiple files with a single key, first package them into an archive using formats like `.ZIP`, `.TAR`, or `.RAR`. Then, encrypt the archive using SeldeanCrypt.

## Notes

- **Security:** Treat your key file as sensitive information. Anyone with access to the key can decrypt your files.
- **Backup:** Always keep a backup of your key file. Losing the key means losing access to your encrypted data.

## Support

For questions, feedback, or support, visit the official website:  
[sertanbalta.com](https://sertanbalta.com)
