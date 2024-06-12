--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: candidate; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidate (
    id integer NOT NULL,
    elect_id integer NOT NULL,
    cand_id character varying(20) NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    middlename character varying(45) NOT NULL,
    address character varying(100) NOT NULL,
    tel character varying(20) NOT NULL,
    "position" character varying(45) NOT NULL,
    party character varying(100) NOT NULL,
    filing_date date NOT NULL
);


ALTER TABLE public.candidate OWNER TO postgres;

--
-- Name: candidate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidate_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.candidate_id_seq OWNER TO postgres;

--
-- Name: candidate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidate_id_seq OWNED BY public.candidate.id;


--
-- Name: election; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.election (
    id integer NOT NULL,
    election_date date NOT NULL,
    status character varying(10) NOT NULL,
    total_voters integer NOT NULL
);


ALTER TABLE public.election OWNER TO postgres;

--
-- Name: election_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.election_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.election_id_seq OWNER TO postgres;

--
-- Name: election_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.election_id_seq OWNED BY public.election.id;


--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    id integer NOT NULL,
    username character varying(45),
    password character varying(45)
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_id_seq OWNER TO postgres;

--
-- Name: login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_id_seq OWNED BY public.login.id;


--
-- Name: member; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.member (
    id integer NOT NULL,
    firstname character varying(45) NOT NULL,
    lastname character varying(45) NOT NULL,
    middlename character varying(45) NOT NULL,
    email character varying(45) NOT NULL,
    mobile character varying(45) NOT NULL,
    role integer NOT NULL,
    member_date date NOT NULL
);


ALTER TABLE public.member OWNER TO postgres;

--
-- Name: vote; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vote (
    id integer NOT NULL,
    voter_id character varying(45) NOT NULL,
    election_id integer NOT NULL,
    cand_id character varying(20) NOT NULL,
    vote_time time without time zone NOT NULL
);


ALTER TABLE public.vote OWNER TO postgres;

--
-- Name: vote_count; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vote_count (
    id integer NOT NULL,
    election_id integer NOT NULL,
    precinct character varying(45) NOT NULL,
    final_tally integer NOT NULL,
    approved_date date NOT NULL
);


ALTER TABLE public.vote_count OWNER TO postgres;

--
-- Name: vote_count_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vote_count_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vote_count_id_seq OWNER TO postgres;

--
-- Name: vote_count_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vote_count_id_seq OWNED BY public.vote_count.id;


--
-- Name: vote_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vote_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vote_id_seq OWNER TO postgres;

--
-- Name: vote_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vote_id_seq OWNED BY public.vote.id;


--
-- Name: voter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.voter (
    id integer NOT NULL,
    mid integer NOT NULL,
    voter_id character varying(45) NOT NULL,
    precinct character varying(45) NOT NULL,
    last_vote_date date NOT NULL
);


ALTER TABLE public.voter OWNER TO postgres;

--
-- Name: voter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.voter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.voter_id_seq OWNER TO postgres;

--
-- Name: voter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.voter_id_seq OWNED BY public.voter.id;


--
-- Name: candidate id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate ALTER COLUMN id SET DEFAULT nextval('public.candidate_id_seq'::regclass);


--
-- Name: election id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.election ALTER COLUMN id SET DEFAULT nextval('public.election_id_seq'::regclass);


--
-- Name: login id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login ALTER COLUMN id SET DEFAULT nextval('public.login_id_seq'::regclass);


--
-- Name: vote id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote ALTER COLUMN id SET DEFAULT nextval('public.vote_id_seq'::regclass);


--
-- Name: vote_count id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote_count ALTER COLUMN id SET DEFAULT nextval('public.vote_count_id_seq'::regclass);


--
-- Name: voter id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter ALTER COLUMN id SET DEFAULT nextval('public.voter_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
6711f7ac3cf9
\.


--
-- Data for Name: candidate; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.candidate (id, elect_id, cand_id, firstname, lastname, middlename, address, tel, "position", party, filing_date) FROM stdin;
1	1	PHL-103	Kristin	Belo	Dua	Pasig City	0988-888-2209	Congressperson	Dutae	2021-10-15
2	1	PHL-101	Joanna	Cruz	Luz	Pasig City	0988-888-8909	President	Dutae	2021-10-15
3	1	PHL-102	Willie	Manto	Cruz	Pasig City	0988-888-9009	Vice-President	Dutae	2021-10-15
\.


--
-- Data for Name: election; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.election (id, election_date, status, total_voters) FROM stdin;
1	2022-05-09	created	0
\.


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (id, username, password) FROM stdin;
1	admin	admin
2	sjctrags	sjctrags
3	owen	owen
4	john	john
5	anna	anna
6	jerry	jerry
7	joel	joel
8	jenny	jenny
12	kris	kris
13	luz	luz
14	user-1908	pass9087
15	user-1908	pass9087
16	user-1908	pass9087
17	user-1908	pass9087
\.


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.member (id, firstname, lastname, middlename, email, mobile, role, member_date) FROM stdin;
1	Juan	Luna	Lopez	juanluna@gmail.com	0922-890-5566	0	1950-07-02
2	Sherwin	Calleja	Tragura	sjctrags@gmail.com	0922-890-5566	0	1978-10-30
3	Owen	Estabillo	Salazar	owen@gmail.com	0922-890-5566	1	1981-07-02
4	John	Cruz	Millari	john@gmail.com	0922-890-5566	1	1980-09-12
5	Anna Jane	Wintour	Elle	anna@gmail.com	0922-111-5324	1	1976-09-05
\.


--
-- Data for Name: vote; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vote (id, voter_id, election_id, cand_id, vote_time) FROM stdin;
1	BCH-111-789	1	PHL-101	10:11:33
2	BCH-111-789	1	PHL-102	09:11:19
\.


--
-- Data for Name: vote_count; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vote_count (id, election_id, precinct, final_tally, approved_date) FROM stdin;
1	1	109-A	5000	2022-05-09
2	1	200-B	6001	2022-05-09
3	1	102	789	2023-07-26
4	1	123	678	2023-07-27
5	1	110-B	8000	2024-10-10
6	1	110-C	6000	2024-10-10
9	1	111-C	6000	2024-10-10
\.


--
-- Data for Name: voter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.voter (id, mid, voter_id, precinct, last_vote_date) FROM stdin;
1	2	BCH-111-789	109-A	2022-05-09
\.


--
-- Name: candidate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.candidate_id_seq', 3, true);


--
-- Name: election_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.election_id_seq', 1, true);


--
-- Name: login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_id_seq', 17, true);


--
-- Name: vote_count_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vote_count_id_seq', 10, true);


--
-- Name: vote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vote_id_seq', 2, true);


--
-- Name: voter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.voter_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: candidate candidate_cand_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_cand_id_key UNIQUE (cand_id);


--
-- Name: candidate candidate_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_pkey PRIMARY KEY (id);


--
-- Name: election election_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.election
    ADD CONSTRAINT election_pkey PRIMARY KEY (id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (id);


--
-- Name: member member_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_pkey PRIMARY KEY (id);


--
-- Name: vote_count vote_count_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote_count
    ADD CONSTRAINT vote_count_pkey PRIMARY KEY (id);


--
-- Name: vote_count vote_count_precinct_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote_count
    ADD CONSTRAINT vote_count_precinct_key UNIQUE (precinct);


--
-- Name: vote vote_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote
    ADD CONSTRAINT vote_pkey PRIMARY KEY (id);


--
-- Name: voter voter_mid_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_mid_key UNIQUE (mid);


--
-- Name: voter voter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_pkey PRIMARY KEY (id);


--
-- Name: voter voter_voter_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_voter_id_key UNIQUE (voter_id);


--
-- Name: candidate candidate_elect_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate
    ADD CONSTRAINT candidate_elect_id_fkey FOREIGN KEY (elect_id) REFERENCES public.election(id);


--
-- Name: member member_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_id_fkey FOREIGN KEY (id) REFERENCES public.login(id);


--
-- Name: vote vote_cand_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote
    ADD CONSTRAINT vote_cand_id_fkey FOREIGN KEY (cand_id) REFERENCES public.candidate(cand_id);


--
-- Name: vote_count vote_count_election_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote_count
    ADD CONSTRAINT vote_count_election_id_fkey FOREIGN KEY (election_id) REFERENCES public.election(id);


--
-- Name: vote vote_election_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote
    ADD CONSTRAINT vote_election_id_fkey FOREIGN KEY (election_id) REFERENCES public.election(id);


--
-- Name: vote vote_voter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vote
    ADD CONSTRAINT vote_voter_id_fkey FOREIGN KEY (voter_id) REFERENCES public.voter(voter_id);


--
-- Name: voter voter_mid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.voter
    ADD CONSTRAINT voter_mid_fkey FOREIGN KEY (mid) REFERENCES public.member(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

