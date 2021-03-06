PGDMP         1            
    y            IluminacionResidencial    13.2    13.2 0    ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    25373    IluminacionResidencial    DATABASE     }   CREATE DATABASE "IluminacionResidencial" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United Kingdom.1252';
 (   DROP DATABASE "IluminacionResidencial";
                postgres    false            ?            1259    25400    distribuidor    TABLE     ?   CREATE TABLE public.distribuidor (
    iddistribuidor integer NOT NULL,
    nombredistribuidor character varying(20) NOT NULL,
    correo character varying(20),
    telefono integer NOT NULL,
    direccion character varying(30) NOT NULL
);
     DROP TABLE public.distribuidor;
       public         heap    postgres    false            ?            1259    25398    distribuidor_iddistribuidor_seq    SEQUENCE     ?   CREATE SEQUENCE public.distribuidor_iddistribuidor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.distribuidor_iddistribuidor_seq;
       public          postgres    false    207            ?           0    0    distribuidor_iddistribuidor_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.distribuidor_iddistribuidor_seq OWNED BY public.distribuidor.iddistribuidor;
          public          postgres    false    206            ?            1259    25392    empleado    TABLE     ?   CREATE TABLE public.empleado (
    idempleado integer NOT NULL,
    nombreempleado character varying(30) NOT NULL,
    edad integer NOT NULL,
    sueldo integer NOT NULL
);
    DROP TABLE public.empleado;
       public         heap    postgres    false            ?            1259    25390    empleado_idempleado_seq    SEQUENCE     ?   CREATE SEQUENCE public.empleado_idempleado_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.empleado_idempleado_seq;
       public          postgres    false    205            ?           0    0    empleado_idempleado_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.empleado_idempleado_seq OWNED BY public.empleado.idempleado;
          public          postgres    false    204            ?            1259    25412    produce    TABLE     ?   CREATE TABLE public.produce (
    idproducto integer NOT NULL,
    idventa integer NOT NULL,
    idsucursal integer NOT NULL,
    nombreproducto character varying(30) NOT NULL,
    cantidad integer NOT NULL,
    precio numeric(6,2) NOT NULL
);
    DROP TABLE public.produce;
       public         heap    postgres    false            ?            1259    25376    stock    TABLE     ?   CREATE TABLE public.stock (
    idproducto integer NOT NULL,
    nombreproducto character varying(30) NOT NULL,
    cantidadproducto integer NOT NULL,
    precio numeric(6,2) NOT NULL,
    iddistribuidor integer
);
    DROP TABLE public.stock;
       public         heap    postgres    false            ?            1259    25374    stock_idproducto_seq    SEQUENCE     ?   CREATE SEQUENCE public.stock_idproducto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.stock_idproducto_seq;
       public          postgres    false    201            ?           0    0    stock_idproducto_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.stock_idproducto_seq OWNED BY public.stock.idproducto;
          public          postgres    false    200            ?            1259    25382    sucursal    TABLE     ?   CREATE TABLE public.sucursal (
    idsucursal integer NOT NULL,
    nombresucursal character varying(20) NOT NULL,
    direccion character varying(30) NOT NULL,
    telefono integer
);
    DROP TABLE public.sucursal;
       public         heap    postgres    false            ?            1259    25380    sucursal_idsucursal_seq    SEQUENCE     ?   CREATE SEQUENCE public.sucursal_idsucursal_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.sucursal_idsucursal_seq;
       public          postgres    false    203            ?           0    0    sucursal_idsucursal_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.sucursal_idsucursal_seq OWNED BY public.sucursal.idsucursal;
          public          postgres    false    202            ?            1259    25432    tiene    TABLE        CREATE TABLE public.tiene (
    idproducto integer NOT NULL,
    idsucursal integer NOT NULL,
    cantidad integer NOT NULL
);
    DROP TABLE public.tiene;
       public         heap    postgres    false            ?            1259    25408    venta    TABLE     ?   CREATE TABLE public.venta (
    idventa integer NOT NULL,
    hora timestamp without time zone NOT NULL,
    total numeric(7,2) NOT NULL
);
    DROP TABLE public.venta;
       public         heap    postgres    false            ?            1259    25406    venta_idventa_seq    SEQUENCE     ?   CREATE SEQUENCE public.venta_idventa_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.venta_idventa_seq;
       public          postgres    false    209            ?           0    0    venta_idventa_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.venta_idventa_seq OWNED BY public.venta.idventa;
          public          postgres    false    208            E           2604    25403    distribuidor iddistribuidor    DEFAULT     ?   ALTER TABLE ONLY public.distribuidor ALTER COLUMN iddistribuidor SET DEFAULT nextval('public.distribuidor_iddistribuidor_seq'::regclass);
 J   ALTER TABLE public.distribuidor ALTER COLUMN iddistribuidor DROP DEFAULT;
       public          postgres    false    207    206    207            D           2604    25395    empleado idempleado    DEFAULT     z   ALTER TABLE ONLY public.empleado ALTER COLUMN idempleado SET DEFAULT nextval('public.empleado_idempleado_seq'::regclass);
 B   ALTER TABLE public.empleado ALTER COLUMN idempleado DROP DEFAULT;
       public          postgres    false    205    204    205            B           2604    25379    stock idproducto    DEFAULT     t   ALTER TABLE ONLY public.stock ALTER COLUMN idproducto SET DEFAULT nextval('public.stock_idproducto_seq'::regclass);
 ?   ALTER TABLE public.stock ALTER COLUMN idproducto DROP DEFAULT;
       public          postgres    false    200    201    201            C           2604    25385    sucursal idsucursal    DEFAULT     z   ALTER TABLE ONLY public.sucursal ALTER COLUMN idsucursal SET DEFAULT nextval('public.sucursal_idsucursal_seq'::regclass);
 B   ALTER TABLE public.sucursal ALTER COLUMN idsucursal DROP DEFAULT;
       public          postgres    false    203    202    203            F           2604    25411    venta idventa    DEFAULT     n   ALTER TABLE ONLY public.venta ALTER COLUMN idventa SET DEFAULT nextval('public.venta_idventa_seq'::regclass);
 <   ALTER TABLE public.venta ALTER COLUMN idventa DROP DEFAULT;
       public          postgres    false    209    208    209            ?          0    25400    distribuidor 
   TABLE DATA           g   COPY public.distribuidor (iddistribuidor, nombredistribuidor, correo, telefono, direccion) FROM stdin;
    public          postgres    false    207   /7       ?          0    25392    empleado 
   TABLE DATA           L   COPY public.empleado (idempleado, nombreempleado, edad, sueldo) FROM stdin;
    public          postgres    false    205   L7       ?          0    25412    produce 
   TABLE DATA           d   COPY public.produce (idproducto, idventa, idsucursal, nombreproducto, cantidad, precio) FROM stdin;
    public          postgres    false    210   i7       ?          0    25376    stock 
   TABLE DATA           e   COPY public.stock (idproducto, nombreproducto, cantidadproducto, precio, iddistribuidor) FROM stdin;
    public          postgres    false    201   ?7       ?          0    25382    sucursal 
   TABLE DATA           S   COPY public.sucursal (idsucursal, nombresucursal, direccion, telefono) FROM stdin;
    public          postgres    false    203   ?9       ?          0    25432    tiene 
   TABLE DATA           A   COPY public.tiene (idproducto, idsucursal, cantidad) FROM stdin;
    public          postgres    false    211   :       ?          0    25408    venta 
   TABLE DATA           5   COPY public.venta (idventa, hora, total) FROM stdin;
    public          postgres    false    209   ":       ?           0    0    distribuidor_iddistribuidor_seq    SEQUENCE SET     N   SELECT pg_catalog.setval('public.distribuidor_iddistribuidor_seq', 1, false);
          public          postgres    false    206            ?           0    0    empleado_idempleado_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.empleado_idempleado_seq', 1, false);
          public          postgres    false    204            ?           0    0    stock_idproducto_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.stock_idproducto_seq', 45, true);
          public          postgres    false    200            ?           0    0    sucursal_idsucursal_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.sucursal_idsucursal_seq', 1, false);
          public          postgres    false    202            ?           0    0    venta_idventa_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.venta_idventa_seq', 1, false);
          public          postgres    false    208            N           2606    25405    distribuidor distribuidor_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.distribuidor
    ADD CONSTRAINT distribuidor_pkey PRIMARY KEY (iddistribuidor);
 H   ALTER TABLE ONLY public.distribuidor DROP CONSTRAINT distribuidor_pkey;
       public            postgres    false    207            L           2606    25397    empleado empleado_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.empleado
    ADD CONSTRAINT empleado_pkey PRIMARY KEY (idempleado);
 @   ALTER TABLE ONLY public.empleado DROP CONSTRAINT empleado_pkey;
       public            postgres    false    205            H           2606    25389    stock stock_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.stock
    ADD CONSTRAINT stock_pkey PRIMARY KEY (idproducto);
 :   ALTER TABLE ONLY public.stock DROP CONSTRAINT stock_pkey;
       public            postgres    false    201            J           2606    25387    sucursal sucursal_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.sucursal
    ADD CONSTRAINT sucursal_pkey PRIMARY KEY (idsucursal);
 @   ALTER TABLE ONLY public.sucursal DROP CONSTRAINT sucursal_pkey;
       public            postgres    false    203            P           2606    25421    venta venta_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_pkey PRIMARY KEY (idventa);
 :   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_pkey;
       public            postgres    false    209            Q           2606    25415    produce fk_produce_producto    FK CONSTRAINT     ?   ALTER TABLE ONLY public.produce
    ADD CONSTRAINT fk_produce_producto FOREIGN KEY (idproducto) REFERENCES public.stock(idproducto);
 E   ALTER TABLE ONLY public.produce DROP CONSTRAINT fk_produce_producto;
       public          postgres    false    201    2888    210            S           2606    25427    produce fk_produce_sucursal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.produce
    ADD CONSTRAINT fk_produce_sucursal FOREIGN KEY (idsucursal) REFERENCES public.sucursal(idsucursal);
 E   ALTER TABLE ONLY public.produce DROP CONSTRAINT fk_produce_sucursal;
       public          postgres    false    2890    203    210            R           2606    25422    produce fk_produce_venta    FK CONSTRAINT     |   ALTER TABLE ONLY public.produce
    ADD CONSTRAINT fk_produce_venta FOREIGN KEY (idventa) REFERENCES public.venta(idventa);
 B   ALTER TABLE ONLY public.produce DROP CONSTRAINT fk_produce_venta;
       public          postgres    false    209    2896    210            U           2606    25440    tiene fk_tiene_producto    FK CONSTRAINT     ?   ALTER TABLE ONLY public.tiene
    ADD CONSTRAINT fk_tiene_producto FOREIGN KEY (idproducto) REFERENCES public.stock(idproducto);
 A   ALTER TABLE ONLY public.tiene DROP CONSTRAINT fk_tiene_producto;
       public          postgres    false    211    2888    201            T           2606    25435    tiene fk_tiene_sucursal    FK CONSTRAINT     ?   ALTER TABLE ONLY public.tiene
    ADD CONSTRAINT fk_tiene_sucursal FOREIGN KEY (idsucursal) REFERENCES public.sucursal(idsucursal);
 A   ALTER TABLE ONLY public.tiene DROP CONSTRAINT fk_tiene_sucursal;
       public          postgres    false    211    2890    203            ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?      ?   R  x?m?M??0???)t???o{??I?ώ??S+?I(??p?0?m?eXO?O?[?????}t?I???[o??M??ؚ1????]\k?!?b	K???r??Rθ"??G?ħp?????݊8Y#?W??RsE?
aym?&ھu?m3iDQ;$#%???g?9?غ?E䳜͂]x	=??̐???_?~?\tGPe(2?]lmT?j???r?]l.?F:x?jn????0\*?T?ܴ?t??\? lR?? ?E?ZeZ.+Ǧ'??+(*<?X-`?FO?U?????9?c??z???B?l?B?~??!Gx?? q?L???P?|J.????*잻q=?g]?E^??]K`D"?Ȝ?O1????$C?Y
?xU#.???k;?ar??|?1x???
?+?,'?u???k?1?F???'{?{i?4<i>??????^??"I7_W?2?wa\N?IR	=??׎!ыQt???9JC?ee!?dS??chT??F??( a???[
?9?H??we??̧?W?]a??? ???ó??n ??9	?Tc^M?aI_?b?@?޾??n?U??T??????g?n 7??e]???o?      ?      x?????? ? ?      ?      x?????? ? ?      ?      x?????? ? ?     