PGDMP     	    &                y            coffee_shop    13.1    13.1     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16868    coffee_shop    DATABASE     o   CREATE DATABASE coffee_shop WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE coffee_shop;
                postgres    false            ?            1259    16869    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            ?            1259    17593    drink    TABLE     ?   CREATE TABLE public.drink (
    id integer NOT NULL,
    title character varying(80),
    recipe character varying(180) NOT NULL
);
    DROP TABLE public.drink;
       public         heap    postgres    false            ?            1259    17591    drink_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.drink_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.drink_id_seq;
       public          postgres    false    202            ?           0    0    drink_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.drink_id_seq OWNED BY public.drink.id;
          public          postgres    false    201            &           2604    17596    drink id    DEFAULT     d   ALTER TABLE ONLY public.drink ALTER COLUMN id SET DEFAULT nextval('public.drink_id_seq'::regclass);
 7   ALTER TABLE public.drink ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    202    201    202            ?          0    16869    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    200   ?       ?          0    17593    drink 
   TABLE DATA           2   COPY public.drink (id, title, recipe) FROM stdin;
    public          postgres    false    202   ?       ?           0    0    drink_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.drink_id_seq', 7, true);
          public          postgres    false    201            (           2606    16873 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    200            *           2606    17598    drink drink_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.drink
    ADD CONSTRAINT drink_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.drink DROP CONSTRAINT drink_pkey;
       public            postgres    false    202            ,           2606    17600    drink drink_title_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public.drink
    ADD CONSTRAINT drink_title_key UNIQUE (title);
 ?   ALTER TABLE ONLY public.drink DROP CONSTRAINT drink_title_key;
       public            postgres    false    202            ?      x?????? ? ?      ?   V   x?3?t?OKKM匮V?K?MU?RPJ?(??X9?E ?????l?HAbQI1PĨ6?ː?'57?Y+X EgejNN~9?VC??=... $     