---
description: This page describes the architecture of the local database
---

# Database

The data is stored in one database, in the /data folder

This database is made up of 3 main tables:

* Metadata table, to store information at the pdf level (author, title, year...)
* Chunk table, to store the chunks before embedding and relevant informations regarding the chunks
* Embedding table, built with sqlite-vec special extension, that only has 2 columns: primary key (shared with chunk table) and embeddings

The process is the following:

* a pdf is added
  * a copy of it is stored
  * its metadata are extracted and stored into the metadata table
* the pdf is processed
  * the chunks are extracted and stored into the chunk table
  * the indexes of these chunks are kept in memory
* the embeddings are computed
  * the chunks are extracted using their indexes and embedded
  * the embeddings are stored, using the indexes as primary keys
* retrieval
  * join the tables, query using vec search, extract chunks
