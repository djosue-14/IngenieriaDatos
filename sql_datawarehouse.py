DDL_QUERY = '''
drop table if exists venta_fact;
drop table if exists dim_usuario;
drop table if exists dim_fecha;
drop table if exists dim_cliente;
drop table if exists dim_articulo;

create table dim_articulo
(
    sk_articulo int          not null,
    id_articulo int          not null,
    codigo      varchar(50)  not null,
    nombre      varchar(255) not null,
    categoria   varchar(50)  not null
);

alter table dim_articulo
    add constraint pk_dim_articulo primary key (sk_articulo);

alter table dim_articulo
    modify column sk_articulo int not null auto_increment;

create table dim_cliente
(
    sk_cliente   int          not null,
    id_cliente   int          not null,
    nombre       varchar(100) not null,
    tipo_persona varchar(20)  not null
);

alter table dim_cliente
    add constraint pk_dim_cliente primary key (sk_cliente);

alter table dim_cliente
    modify column sk_cliente int not null auto_increment;

create table dim_usuario
(
    sk_usuario int          not null,
    id_usuario int          not null,
    nombre     varchar(100) not null,
    estado     varchar(10)  not null,
    rol        varchar(30)  not null
);

alter table dim_usuario
    add constraint pk_dim_usuario primary key (sk_usuario);

alter table dim_usuario
    modify column sk_usuario int not null auto_increment;

create table dim_fecha
(
    id_date      int         not null,
    full_date    datetime    not null,
    year         int         not null,
    month        int         not null,
    quarter      int         not null,
    day          int         not null,
    week         int         not null,
    day_of_week  int         not null,
    day_name     varchar(15) not null,
    weekday_flag varchar(10) not null,
    month_name   varchar(20) not null
);

alter table dim_fecha
    add constraint pk_dim_fecha primary key (id_date);

create table venta_fact
(
    id_venta       int not null,
    sk_cliente     int not null, -- dim cliente
    sk_usuario     int not null, -- dim usuario
    id_fecha_venta int not null, -- dim fecha
    sk_articulo    int not null, -- dim articulo
    total          decimal(11, 2),
    descuento      decimal(11, 2),
    estado         varchar(10)
);

alter table venta_fact
    add constraint pk_venta_fact primary key (id_venta, sk_cliente, sk_usuario, id_fecha_venta, sk_articulo);

alter table venta_fact
    add constraint fk_venta_fact_dim_cliente foreign key (sk_cliente) references dim_cliente(sk_cliente);

alter table venta_fact
    add constraint fk_venta_fact_dim_usuario foreign key (sk_usuario) references dim_usuario(sk_usuario);

alter table venta_fact
    add constraint fk_venta_fact_dim_fecha foreign key (id_fecha_venta) references dim_fecha(id_date);

alter table venta_fact
    add constraint fk_venta_fact_dim_articulo foreign key (sk_articulo) references dim_articulo(sk_articulo);
'''