create database bank_management;
use bank_management;

create table Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(20), 
    email varchar(50),
    phone varchar(50)
);
select * from Customers;

create table account (
    Acc_no int primary key,
    customer_id int,
    acc_type varchar(20),
    balance int,
    foreign key (customer_id) references Customers(customer_id)
);

create table transaction (
    Acc_no int,
    transaction_type varchar(20),
    amount int,
    transaction_date datetime,
    foreign key (Acc_no) references account(Acc_no) -- Corrected foreign key reference here
);

insert into Customers values
(1,'rrk', 'singh', 'rrk7808746144@gmail.com', 9110921756),
(2,'munna', 'kumar', 'mingkingtube@gmail.com', 14567890),
(3,'rohit', 'kumar', 'rohitkr@gmail.com', 85236970);

insert into account values
(101, 1, 'Savings', 1000),
(102, 2, 'current', 2000),
(103, 3, 'Savings', 3000);

insert into transaction values
(101, 'Deposit', 500, CURRENT_TIMESTAMP),
(102, 'withdraw', 500, CURRENT_TIMESTAMP),
(103, 'Deposit', 500, CURRENT_TIMESTAMP);


select * from Customers;

select * from account;
select * from transaction;

