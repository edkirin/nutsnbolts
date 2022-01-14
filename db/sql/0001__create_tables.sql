CREATE TABLE IF NOT EXISTS public.nuts (
    id serial PRIMARY KEY,
    counter int NULL
);
ALTER TABLE public.nuts OWNER TO nutsnbolts;

CREATE TABLE IF NOT EXISTS public.bolts (
    id serial PRIMARY KEY,
    counter int NULL
);
ALTER TABLE public.bolts OWNER TO nutsnbolts;
