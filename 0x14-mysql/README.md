# Project Documentation: MySQL Setup and Management

---

## Introduction

This documentation outlines the setup and management procedures for MySQL databases on servers web-01 and web-02. The project aims to establish a primary-replica infrastructure using MySQL, ensuring redundancy and load distribution for improved database reliability and performance. Additionally, it includes procedures for database backup to safeguard against data loss in the event of server failures or disasters.

---

## Project Structure

1. **Task 0: Install MySQL:**
   - **Purpose:** Install MySQL 5.7.x on servers web-01 and web-02.
   - **Verification:** Check MySQL version using `mysql --version`.

2. **Task 1: Let us in!:**
   - **Purpose:** Create a MySQL user `holberton_user` on both servers with permissions to check primary/replica status.
   - **Verification:** Show grants for the created user to verify permissions.

3. **Task 2: If only you could see what I've seen with your eyes:**
   - **Purpose:** Create a database `tyrell_corp` with a table `nexus6` and add at least one entry for replication setup.
   - **Verification:** Query the table to ensure it exists and is not empty.

4. **Task 3: Quite an experience to live in fear, isn't it?:**
   - **Purpose:** Create a new user `replica_user` on web-01 with appropriate permissions for replication.
   - **Verification:** Check privileges for `replica_user` using `mysql.user`.

5. **Task 4: Setup a Primary-Replica infrastructure using MySQL:**
   - **Purpose:** Establish replication between web-01 (primary) and web-02 (replica) for the `tyrell_corp` database.
   - **Configuration:** Provide MySQL primary and replica configuration files (`my.cnf` or `mysqld.cnf`).
   - **Verification:** Verify replication status on both servers using `SHOW MASTER STATUS` and `SHOW SLAVE STATUS`.

6. **Task 5: MySQL backup:**
   - **Purpose:** Create a Bash script to generate MySQL dump, compress it, and store it as a backup.
   - **Requirements:** Dump all databases to `backup.sql`, compress to `day-month-year.tar.gz`.
   - **Verification:** Check generated dump and compressed archive.

---

## Learning Objectives

Upon completion of this project, learners are expected to:

- Understand the main role of a database and its importance in application development.
- Recognize the purpose of a database replica in ensuring redundancy and load distribution.
- Appreciate the necessity of storing database backups in different physical locations for disaster recovery.
- Perform regular checks on database backup strategies to ensure their effectiveness and reliability.

---

This documentation provides a comprehensive guide to setting up and managing MySQL databases, including installation, user management, replication setup, and backup strategies. By following the outlined procedures, users can ensure the availability, reliability, and security of their MySQL databases, contributing to the overall success of their projects.
