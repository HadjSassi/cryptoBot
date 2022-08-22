create table User (
id int auto_increment unique,
username varchar(255) unique,
email varchar(255) unique,
password varchar(255),
primary key (id, username)
);

create table Bots (
id int unique primary key,
nom_bot varchar(255) unique,
user_name varchar(255),
constraint fk_bots foreign key (user_name) references user(username)
);


create table Params_bot_Cocotier (
id int unique primary key,
 name_bot varchar(255),
api_key varchar(255),
secret_key varchar(255),
delta_hour varchar(255),
type_computing enum('n-1','n-2','n-3'),
market varchar(255),
constraint fk_params_bot_cocotier foreign key (name_bot) references bots(nom_bot)
);

create table Params_bot_trix (
id int unique primary key,
 name_bot varchar(255),
 api_key varchar(255),
secret_key varchar(255),
subaccount varchar(255),
trixlenght_conf int default 9,
trixsignal_conf int default 21,
stochTop_conf float(3,2) default 0.88,
stochBottom_conf float(3,2) default 0.15,
stochRSI_conf int default 13,
bot_name varchar(255) default 'anisse bot',
user_name varchar(255) default 'helmi',
sql_password varchar(255) default 'Magali_1984',
constraint fk_params_bot_trix foreign key (name_bot) references bots(nom_bot)
);

create table get_balence (
id int primary key,
dates date,
times time,
user_name varchar(255),
bot_name varchar(255),
actual_crypto_balence varchar(255),
crypto_name varchar (255), 
crypto_wallet varchar(255)
);
