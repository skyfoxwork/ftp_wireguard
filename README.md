# FTP WIREGUARD

## Description
Project use vpn (wireguard) and ftp

## Technologies

- Python 3
- Wireguard (vpn)

## **Make commands (Makefile):**
```shell
make build       # Build docker image
make run         # Run container
```

### **How to Run the Project**

Follow these steps to set up and run the project on your local machine.
You can run project with 2 ways (with Docker or with Postgres directly)

---
### **Run the Project with Docker**

Install Python3:

```shell
www.python.org/
```

Install Git:

```shell
https://git-scm.com/
```

Install Docker:

```shell
https://www.docker.com/
```

#### **1. Clone the Repository**

Start by cloning the project repository from GitHub:

```bash
git clone <url>
```
```shell
cd ftp_wireguard
```

```shell
git checkout develop
```
---

#### **2. Create and Activate a Virtual Environment**

It is recommended to use a virtual environment to isolate project dependencies:

Create virtual environment:

```shell
python3 -m venv venv
```

Activate virtual environment (venv).

MacOS, Linux:

```shell
source venv/bin/activate
```
   Windows:

```shell
venv\Scripts\activate
```

---

#### **4. Create a `.env` File**

Create a .env file in the root of the project and add the following environment variables:

Create .env file
```shell
cp .env.example .env
```

add data to .env.
```env
## FTP
FTP_HOST=add_data
FTP_USER=add_data
FTP_PASSWORD=add_data

## wireguard
# [Interface]
WG_ADDRESS=add_data
WG_PRIVATEKEY=add_data
WG_LISTENPORT=add_data
WG_DNS=add_data

# [Peer]
WG_PUBLICKEY=add_data
WG_ENDPOINT=add_data
WG_ALLOWEDIPS=add_data
WG_PERSISTENKEEPALIVE=add_data
```

#### **5. Run the Project with Docker**
(Linux, MacOS)
```bash
make build
make run
```

or use commands (Linux, MacOS, Windows):
```bash
docker build -t ftp_wireguard .
docker run --rm -it --cap-add=NET_ADMIN --cap-add=MKNOD --env-file .env ftp_wireguard
```
