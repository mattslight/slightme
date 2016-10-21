MODERN DATA SCIENCE FOR BUSINESS
================================
* A study of the current business intelligence and related landscapes, prepared by Slight Data Science LLC. *

Contents
--------
0. Executive Summary
1. Rationale of Data Science
2. Traditional Models and Shortfalls
3. Modern Models and Advantages
..1. Advances in Technology
..2. Software Paradigm Changes
..3. Changes in Business Practice
..4. Summary
4. The Core Data Science Competencies
..1. Collection
..2. Storage (& Injestion)
..3. Transposition
..4. Analysis
..5. Presentation
..6. Interaction
5. Current Business Landscape
..1. Big Data & Hadoop
..2. Open vs. Proprietary
..3. Python vs. R
..4. Machine Learning
6. Business Implications
7, Practical Applications
8. Summary

2 Traditional BI Models and Shortfalls
--------------------------------------
The traditional model of data science application within business is marked by the business disciplines / functions known as Data-Warehousing (commonly DW or DWH) and Business Intelligence (BI). Where large amount of data are involed (billions of rows upwards), it may also be termed 'Big Data'. The split beween DW and BI (together referred to as DW/BI) represents the bottom up and top down approach of solutions from a technical architecture perspective. DW being the bottom-up approach of the design and *architecture* from a data curation and storage perspective (and the related functions of extraction load and transformation [ETL]). Whilst BI is the top-down *approach* of data consumption starting at the business requirements and usually comprising at least data visualisation and often some form of interaction or querying of data. Where DW and BI converge, from a business persective at least - if not also from a theoretical viewpoint - is a blurred line, in terms of a specific separation of business process or technology application.

Although the distinction between DW and BI per se. may be unclear the complete stack of technologies, processes and methodology is relatively well-defined, even if not always well understood or clearly implemented within business. It has not always been necessary, from a strategic business perspective, or a company to understand academically the data science principals behind the functional process - as long as operationally the components are well defined, properly integrated and a consistent analytical method is used. That said it is clearly advantageous for companies to have analysts and IT professionals conversant in the theoretical data science foundations of DW and BI. Later we will also discuss how the traditional roles of analysts are nowadays becoming known simply as data scientists (especially in technology hubs such as Silicon Valley, California, US), representing the greater emphasis on statistical and empirical methodologies - also reflecting an alignment with the scientific and academic institutions.

The focus of DW and BI in the past has been technical design integration dealing with a mixture of transactional databases and unstructured data sources. In regards to terminology the nature of the differences in data structures is referred to as 'heterogenous data', whereas data of the same strucutre 'homogenous data'). A good example of heterogenous data would be the mixture of financial data and customer sentiment. In contrast homogenous data is all of the same type & structure, an example would be multiple employee records cards. This mixture of data exists within organisations due to the variety of data sources, including variety in software package, vendor formats, database structures, differing data types and so on. This mixture of data is what makes data science so valuable to businesses as it is possible to draw on multiple facts to draw new conclusions to steer business decision making. It is not therefore a desire of modern data science to avoid this mixture of data structures, but to handle it in a better fashion. What this means we will come on to shortly. From the business intelligence perspective the additional challenges of data science revolved around perfomance constaints inherent in the DW layer - specifically the speed by which data can be processed, analysed and queried.

First we describe the traditional data science model in order to highlight the weaknesses, later we compare against the modern model in order to underline the advantages to be gained from newer ways of working (and thinking).

[Image of Traditional DWBI model][1]

[1]:http://image.slidesharecdn.com/01bioverview-151214123258/95/traditional-datawarehousing-bi-overview-6-638.jpg

Although the model appears simple enough in terms of the arcitecture and overall component integration the shortalls are aparent and many:-

1. Complexities within the ETL layer - including schema design, semantic layers etc. leading to complex and highly technical practical applications
2. Storage hardware performance limitations
3. Storage capacity limitations
4. High cost
5. Poor analytics performance (limited compute)
6. Slow query performance (relational database limitations)
7. Restricted networking performance (separation of data )
8. Proprietary hardware/software
9. Lack of mobile and tablet visualisation
10. Technical design of dashboards

*The downfalls created by some of these points are obvious*, whilst others present more subtle challenges, for example propriety software creates vendor lock-in, leading to inflated costs, restriction to choose the most suitable business solution and a reliance on highly technical & specalised staff resources or the need for ongoing 3rd-party support.

Many businesses invested in such a traditional solution experience combinations of the above issues, leading to DW/BI functions which can not keep up with the pace of change and evolution of the modern company. Modern data science practice addresses all of these challenges owing to several advances technology and maturity of a businesses understanding of DS application.

Modern Models &amp; Advantages
------------------------------
Addressing the above challenges can be a daunting task for any business, owing to the quickly changing landscape of options available to overcome them. Underscoring those advancements has been a shift in technology, software and standard practices.

### Advances in Technology
The technology changes can be summarised as:-
1. A reduction in the cost of storage capacity (price per gigabyte) and speed (Solid-State Disks [SSD])
2. Introduction of distributed file (HDFS) and compute (MapReduce) resoruces
3. Availability of low cost, high capacity RAM (including Flash)

Simply put it is now possible for businesses to invest modestly in powerful and fast storage and compute power as standard, i.e. to use off the shelf commodity server hardware. Furthermore it is possible for companies to rent servers on-demand from cloud service providers therefore reducing further the total cost of ownership and effectively outsourcing parts of the support and maintenance of IT allowing the business to focus on the more vaulable data science activities.

### Software Paradigm Changes
Complimenting the advances in technology is corresponding changes in software design of the end-to-end DWBI solutions. The most obvious shift is the availability for software to take advantage of the increases in I/O performance leading to the possibility of real-time ingestion, analysis and consumption of terabytes of data (enabling Big Data analytics). This is achieved without reliance on specialist hardware, instead the primiary software driver being to facilitate the distributed resource sharing of a commodity low-cost server cluster. This has been made possible primarily due to virtualisation of software and hardware (abstraction of compute and storage resources across an array), distrubuted file systems (HDFS), distributed compute engines (MapReduce) and distrubted task scheduling (YARN).

### Changes in Business Practice
Combined with the advances in technology and the software paradigm shift, businesses have had to change the way they approach data analytics. This becomes aparent in the way the management of IT resources need to be deployed and managed, how data collection and consumption occurs and the ways in which anaytics can be performed, queries of the data be made and presentation of data on mobile user devices (laptops, internet connected desktops, smartphones and tablets). These changes are not simply cosmetic and are a long-awaited demand of businesses wanting to address the short-comings of traditional DW/BI solutions. The net impact to the business is more agile processing of data, quicker analytics - leading to real-time decision making. Under the hood businesses require evolving staff skills across IT and functional teams.

### Summary
In summary the improvements over the traditional model are:-

|Improvement|Traditional Area Addressed                  |Business Impact                                        |
|-----------|--------------------------------------------|-------------------------------------------------------|
|Hardware   |Storage speed & capacity cost               |Keep all data (discard nothing)                        |
|Hardware   |Volatile memory (RAM) speed, capacity & cost|Analyse data faster                                    |
|Software   |Distributed resourcing						 |Use commodity hardware, flexible scaling, reduce cost  |
|Software   |Proprietary software and databases			 |Free from vendor lock-in, reduce cost, increase choice |
|Business   |IT staff required for support & maintenance |Deploy business analysts and functional experts        |
|Business   |Slow to process and make decisions on data  |Make informed decisions quickly					     |