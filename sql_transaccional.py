DDL_QUERY =  '''
drop table if exists detalle_ingreso;
drop table if exists ingreso;
drop table if exists detalle_venta;
drop table if exists venta;
drop table if exists articulo;
drop table if exists categoria;
drop table if exists usuario;
drop table if exists rol;
drop table if exists persona;

CREATE TABLE IF NOT EXISTS categoria
(
    id_categoria int          not null,
    nombre       varchar(50)  not null,
    descripcion  varchar(255),
    estado       bit          not null
);

ALTER TABLE categoria
    ADD CONSTRAINT pk_categoria PRIMARY KEY (id_categoria);

CREATE TABLE IF NOT EXISTS articulo
(
    id_articulo  int            not null,
    id_categoria int            not null,
    codigo       varchar(50)    not null,
    nombre       varchar(100)   not null,
    precio_venta decimal(11, 2) not null,
    stock        int            not null,
    descripcion  varchar(255),
    imagen       varchar(50),
    estado       bit            not null
);

alter table articulo
    add constraint pk_articulo primary key (id_articulo);

create table if not exists rol
(
    id_rol      int         not null,
    nombre      varchar(30) not null,
    descripcion varchar(255),
    estado      bit         not null
);

alter table rol
    add constraint pk_rol primary key (id_rol);

create table if not exists usuario
(
    id_usuario     int          not null,
    id_rol         int          not null,
    nombre         varchar(100) not null,
    tipo_documento varchar(20)  not null,
    num_documento  varchar(20)  not null,
    direccion      varchar(70)  not null,
    telefono       varchar(20)  not null,
    email          varchar(50)  not null,
    clave          varchar(255) not null,
    estado         bit          not null
);

alter table usuario
    add constraint pk_usuario primary key (id_usuario);

create table if not exists persona
(
    id_persona     int          not null,
    tipo_persona   varchar(20)  not null,
    nombre         varchar(100) not null,
    tipo_documento varchar(20)  not null,
    num_documento  varchar(20)  not null,
    direccion      varchar(70)  not null,
    telefono       varchar(20)  not null,
    email          varchar(50)  not null
);

alter table persona
    add constraint pk_persona primary key (id_persona);

create table if not exists detalle_venta
(
    id_detalle_venta int            not null,
    id_venta         int            not null,
    id_articulo      int            not null,
    cantidad         int            not null,
    precio           decimal(11, 2) not null,
    descuento        decimal(11, 2) not null
);

alter table detalle_venta
    add constraint pk_detalle_venta primary key (id_detalle_venta);

create table if not exists venta
(
    id_venta          int            not null,
    id_cliente        int            not null,
    id_usuario        int            not null,
    tipo_comprobante  varchar(20)    not null,
    serie_comprobante varchar(7)     not null,
    num_comprobante   varchar(10)    not null,
    fecha             timestamp      not null,
    impuesto          decimal(4, 2)  not null,
    total             decimal(11, 2) not null,
    estado            varchar(20)    not null
);

alter table venta
    add constraint pk_venta primary key (id_venta);

create table if not exists detalle_ingreso
(
    id_detalle_ingreso int            not null,
    id_ingreso         int            not null,
    id_articulo        int            not null,
    cantidad           int            not null,
    precio             decimal(11, 2) not null
);

alter table detalle_ingreso
    add constraint pk_detalle_ingreso primary key (id_detalle_ingreso);

create table if not exists ingreso
(
    id_ingreso        int            not null,
    id_proveedor      int            not null,
    id_usuario         int            not null,
    tipo_comprobante  varchar(20)    not null,
    serie_comprobante varchar(7)     not null,
    num_comprobante   varchar(10)    not null,
    fecha             timestamp      not null,
    impuesto          decimal(4, 2)  not null,
    total             decimal(11, 2) not null,
    estado            varchar(20)    not null
);

alter table ingreso
    add constraint pk_ingreso primary key (id_ingreso);

alter table articulo
    add constraint fk_articulo_categoria foreign key (id_categoria) references categoria(id_categoria);

alter table detalle_venta
    add constraint fk_detalle_venta_venta foreign key (id_venta) references venta(id_venta),
    add constraint fk_detalle_venta_articulo foreign key (id_articulo) references articulo(id_articulo);

alter table detalle_ingreso
    add constraint fk_detalle_ingreso_ingreso foreign key (id_ingreso) references ingreso(id_ingreso),
    add constraint fk_detalle_ingreso_articulo foreign key (id_articulo) references articulo(id_articulo);

alter table venta
    add constraint fk_venta_persona foreign key (id_cliente) references persona(id_persona),
    add constraint fk_venta_usuario foreign key (id_usuario) references usuario(id_usuario);

alter table ingreso
    add constraint fk_ingreso_persona foreign key (id_proveedor) references persona(id_persona),
    add constraint fk_ingreso_usuario foreign key (id_usuario) references usuario(id_usuario);

alter table usuario
    add constraint fk_usuario_rol foreign key (id_rol) references rol(id_rol);
'''