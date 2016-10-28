MODERN DATA SCIENCE FOR BUSINESS
================================
*A study of the current business intelligence and related landscapes, prepared by Slight Data Science LLC.*

Contents
--------
1. Executive Summary
2. Rationale of Data Science
3. Traditional Models and Shortfalls
4. Modern Models and Advantages
5. The Six Core Business Data Science Competencies
6. Current Business Landscape
    1. Big Data & Hadoop
    2. Open vs. Proprietary
    3. Python vs. R
    4. Machine Learning
7. Summary
    1. Business Implications
    2. Practical Application
 

1 Executive summary
-------------------

>> "Data is the Next Intel Inside." ~ Tim O’Reilly 

This whitepaper provides (a) an overview of the current landscape for applied data science within business, (b) an analysis of the tools & modes of application; and (c) an evaluation of the practical implications available to businesses wishing to conduct data science. In fact we argue that every business should conduct effective data science in order to remain competitive beyond 2020.

This report provides the historic context of existing data science applications within business, often commonly referred to within organisations as Data-warehousing (DW) (the procurement, sanitization and abstraction) and Business Intelligence (BI) (the analysis, general consumption and presentation of data). We develop the traditional DW/BI model and explain how advances in hardware and software technology provide cost-effective means of disrupting the foundational assumptions of existing data analytics platforms, both from a technical (IT) and business process orientated perspective. We further explore how these advances increase the consumption and computation of data within business, effectively introducing cost-viable ‘Big-Data’ capabilities. We conclude the study by looking at the total impact of this shift on business resourcing requirements.


###Recommendations from our team

**Firstly,** it is essential for every business wishing to remain competitive to conduct effective data science and analytics techniques. This applies equally to small businesses and large enterprises. It should include at a minimum analysis of customer behaviour, operational efficiency and optimisation of profits.

**Secondly,** whether developing new business competencies or building on existing ones, the business should include key capabilities in six key defined areas. It is recommended that a minimum level of proficiency be achieved in eachh of those areas in order to effectively achieve a solution which holistically meets the basic needs of a modern business. That is to say that a total deficiency in any one of the six core areas of expertise renders any BI solution potentially not fit for purpose.

**Thirdly,** solutions should be approached from a vendor neutral perspective with additional preference given to ‘open’ platforms. Such an approach ensures the future-proofing of the data science function, allows agile upgrading and minimises the total cost of ownership. It is recommended that proprietary resources and techniques which cause vendor lock-in and provided restricted compability with other modules be avoided where practically possible.


2 Rationale of Data Science
---------------------------
*omitted*


3 Traditional BI Models and Shortfalls
--------------------------------------
The traditional model of data science application within business is marked by the business disciplines / functions known as Data-Warehousing (commonly DW or DWH) and Business Intelligence (BI). Where large amount of data are involed (billions of rows upwards) it may also be termed 'Big Data'. The distinction beween DW and BI (together referred to as DW/BI) represents the bottom up and top down approach of solutions from a technical architecture perspective. DW being the bottom-up approach of the design from a data curation and storage perspective (and the related functions of extraction load and transformation [ETL]). Whilst BI is the top-down approach of data consumption starting at the business requirements and usually comprising at least data visualisation and often some form of interaction or querying of data. Where DW and BI converge, from a business persective at least - if not also from a theoretical viewpoint - is a blurred line, in terms of a specific separation of business process or technology application.

Although the distinction between DW and BI per se. in practice may be unclear the complete stack of technologies, processes and methodology are relatively well-defined, even if not always well understood or clearly implemented within business. It has not always been necessary from a strategic business perspective for a company to understand academically the data science principals behind the functional process - as long as operationally the components are well defined, properly integrated and a consistent analytical method is used. That said it is clearly advantageous for companies to have analysts, managers and IT professionals conversant in the foundations of data science theory spanning DW and BI.

The focus of DW and BI in the past has been technical design integration dealing with a mixture of transactional databases and unstructured data sources. *In regards to terminology the nature of the differences in data structures is referred to as 'heterogenous data', whereas data of the same strucutre 'homogenous data'). A good example of heterogenous data would be the mixture of financial data and customer sentiment. In contrast homogenous data is all of the same type & structure, an example would be multiple employee records cards. This mixture of data exists within organisations due to the variety of data sources, including variety in software package, vendor formats, database structures, differing data types and so on.* [a][breakout comment?] The mixture of data types is partly what makes data science so valuable to businesses, as it is possible to draw on multiple facts to draw new conclusions to steer business decision making. It is not therefore a desire of modern data science to avoid this mixture of data structures, but to handle it in a better fashion. What business impact this has we will come on to shortly. From the business intelligence perspective the additional challenges of data science traditionally revolve around perfomance constaints inherent in the DW layer - specifically the speed by which data can be processed, analysed and queried. Modern data science seeks to address these limitations.

### The Traditional Model
First we describe the traditional data science model as applied to most businesss in order to highlight the weaknesses, afterwards we compare this against the modern model to underline the advantages to be gained from newer ways of working (and thinking).

[Image of Traditional DWBI model][1]

[1]:http://image.slidesharecdn.com/01bioverview-151214123258/95/traditional-datawarehousing-bi-overview-6-638.jpg

*Should the traditional model be described a little?*

Although the model appears simple enough in terms of the arcitecture and overall component integration the shortalls are aparent and many:-

1. Complexities within the ETL layer - including schema design, semantic layers etc. leading to complex and highly technical practical applications
2. Storage hardware performance limitations
3. Storage capacity limitations,
4. High cost
5. Poor analytics performance (limited compute)
6. Slow query performance (relational database limitations)
7. Restricted networking performance (separation of data and compute across a network)
8. Proprietary hardware/software
9. Lack of mobile and tablet visualisation
10. Technical design of dashboards

The downfalls caused by some of these constraits are obvious, whilst others present more subtle challenges. Take the example of propriety software which creates vendor lock-in, this leads to inflated costs, restriction to choose the most suitable business solution and a reliance on highly technical & specalised staff resources or the need for ongoing 3rd-party support. Therefore in the traditional model early implementation decisions have significant practical impact later on.

It is common for many businesses invested in such a traditional solution to experience conflations of the above issues, leading to DW/BI functions which can not keep up with the pace of change and evolution of the company. Modern data science practice addresses all of these challenges owing to a combination of technology advances and business maturity of data science understanding.

Modern Models &amp; Advantages
------------------------------
Addressing the above challenges can be a daunting task for any business, due to the quickly changing landscape of options available to combat them. Underscoring those advancements has been a shift in technology, software and standard practices.

### Advances in Technology
The technology changes within BI/DW can be summarised as:-
1. A reduction in the cost of storage capacity (price per gigabyte) and speed (Solid-State Disks [SSD])
2. Introduction of distributed file (HDFS) and compute (MapReduce) resoruces
3. Availability of low cost, high capacity RAM (including Flash)
*convert to a table?*

Simply put it is now possible for businesses to invest modestly in powerful and fast storage and compute power as standard, i.e. to use off the shelf commodity server hardware. Furthermore it is possible for companies to rent servers on-demand from cloud service providers therefore reducing further the total cost of ownership (TCO) and effectively outsourcing parts of the support and maintenance of IT allowing the business to focus on the more vaulable data science activities.

### Software Paradigm Changes
Complimenting the advances in technology is corresponding changes in software design of the end-to-end DW/BI solutions. The most obvious shift is the availability for software to take advantage of the increases in I/O performance leading to the possibility of real-time ingestion, analysis and consumption of terabytes of data (enabling Big Data analytics). This can be achieved without reliance on specialist hardware, instead the primiary software driver is to facilitate the distributed resource sharing of a commodity low-cost server cluster, known as massive parallel processing (MPP). This has been made possible primarily due to virtualisation of software and hardware (abstraction of compute and storage resources across a hardware array), distrubuted file systems (e.g. HDFS), distributed compute engines (e.g. MapReduce) and distrubted task scheduling (e.g. YARN).

### Changes in Business Practice
Combined with the advances in technology and the software paradigm shift, businesses have needed to change the way they approach data analytics. This becomes aparent in the way the management of IT resources need to be deployed and managed, how data collection and consumption occurs, the ways in which anaytics can be performed, queries of the data be made and presentation of data on mobile user devices (laptops, internet connected desktops, smartphones and tablets). These changes are not simply cosmetic and are a long-awaited demand of businesses wanting to address the short-comings of traditional DW/BI solutions. The net impact to the business is more agile processing of data and quicker analytics - leading to real-time decision making. Under-the-hood, businesses staff skills requirements are evolving, especially across IT and functional data consumption teams.

The traditional roles of analysts are becoming known more commonly as data scientists (particularly within technology hubs such as Silicon Valley in the US). This shift is partly due to the greater emphasis on statistical and empirical methodologies - which also echos an alignment with the scientific and academic institutions.

Other changes in business practice are also aparent such as the increased adoption of Open software and hardware, which will be discussed in depth later.

### Summary

>> "Data really powers everything that we do." ~ Jeff Weiner, LinkedIn 

In summary the improvements over the traditional model are:-

|Improvement|Traditional Area Addressed                  |Business Impact                                        |
|-----------|--------------------------------------------|-------------------------------------------------------|
|Hardware   |Storage speed & capacity cost               |Keep all data (discard nothing)                        |
|Hardware   |Volatile memory (RAM) speed, capacity & cost|Analyse data faster                                    |
|Software   |Distributed resourcing						 |Use commodity hardware, flexible scaling, reduce cost  |
|Software   |Proprietary software and databases			 |Free from vendor lock-in, reduce cost, increase choice |
|Business   |IT staff required for support & maintenance |Deploy business analysts and functional experts        |
|Business   |Slow to process and make decisions on data  |Make informed decisions quickly					     |

**TODO How to visualise versus traditional model**

5 Core Business Data Science Competencies
-----------------------------------------
In order that a business achieve a suitable level of data science competency and protect its Return On Investment (ROI) it is not simply sufficient (or necessary) to deploy good hardware, software and business personnel. Rather, those three key components are a means to an end to achieve what the business really wants which is to extract value from data, and allow business decision makers to gain insight from it. Far too many businesses blindly adopt data science, datawharehousing and/or business intelligence only to find that what was employed is either not required, not well suited to the business challenge, or not well understood enough to make use of. In order that a business really gets a solution which is fit for purpose it should understand the six key components and achieve a minimum level of competency in each, in order to extract value from the whole. A good analogy of this would be a car with a tuned engine, efficient fuel system, high performance transmission, employing Micheal Schumaker as driver but not fitting any or suitable tyres. Leaving out any one of the components makes the whole system effectively useless. On the flip-side this presents strategic opportunities for businesses to make improvements to the output (i.e. achieving the competitive business advantage) since it not necessary to upgrade all of the components to increase capability. Extending on from our race-car analogy and as an example, we might choose only to swap out the engine for a newer model due to high mileage or change the tyres say from slick to wet to take advantage of changing race (i.e. business) conditions.

>> "Information is the oil of the 21st century, and analytics is the combustion engine” ~ Peter Sondergaard, Senior Vice President, Gartner

For data science the components are not the engine, tyres, driver etc. but rather the following:-

### Collection

Traditionally data is collected in databases referred to as On-Line Transaction Processing (OLTP). The On-Line part indicating that the database contains active business data and the Transactional Processing referring to the fact that data is recorded as 'transactions'. In a nutshell data is stored in rows and columns in a relational database (commomly SQL). Sometimes the application or service vendor does refer to any OLTP unit or database, or simply does not offer the feature due to specific application design decisions. When electronic formats are available but databases are not accessible, these OLTP stores might be spreadsheets or data files (e.g. CSV) which are written to in a way such as to achieve OLTP. In traditional DW/BI solutions it is difficult to incorporate data which falls outside of the traditional transactional database format, e.g. market research data, sensor data or customer sentiment. It also difficult for those types of data to be collected due to the volume of data requried to gain value from it. More often than not this means companies simply either avoid handling rich data or struggle to get off the ground with its analysis.

>> "With data collection, ‘the sooner the better’ is always the best answer." ~ Marissa Mayer, CEO, Yahoo

Modern techniques allow for data to be collected in realtime and processed 'on-the-fly', further avoiding the need for a specific Extraction process in the traditional ETL model. Modern techniques also make it very easy to collect different types of data both internal and external to the business from a variety of sources.

### Storage (& Injestion)
One limitation of the traditional model is methods of data storage. Usually storing data for "Off-line" processing requries a copy of the data within the datawarehouse, and possibly a third copy of the processed data in a datamart or datalake. Since older hardware has slower access rates and physical limitations on size, the cost of upgrading compatible hardware can be less cost effective than moving entirely to a modern distributed model.

*any evidence to back that up?*

[Traditional Storage &amp; Compute versus Modern][2]

[2]:https://www.mapr.com/sites/default/files/architecture-image02.jpg

The modern DW/BI model stores data at the processing location, therefore significantly reducing network overhead and improving BI performance by orders of magnitude. *what's the study show?*.

Most commonly this is achieved nowadays via the HDFS component of the Hadoop suite. Which in its simplest terms is both a file storage and database mechanism which handles the computation of data at the point of storage. Another benefit is that modern distributed data stores are also capable of handling heterogenous data.


### Transposition
In order to process data it must be transposed or formatted in a standard way, this could include storing financial data in a common base currency, or that times and dates use a consistent format. The drawbacks of traditional Transposition (or Transformation) layers is in their complexity. Often a company must  define data schemas to a proposed standard and ensure that existing data complies and is transformed to adhere to the defined standard. Besides being technically complex, schemas require updating and require specific IT resource overhead.

By contrast the transposition layer is naturally thin in the modern model, owing to the fact that modern data-stores offer greater flexibility. Data is also kept closer to it's point of analysis and due to improved performance can be transposed where requried at the time of analysis rather than in advance like in the traditional model. Since modern transposition layers are very thin the demand on IT within the business is minimal, freeing up resources for the business and reducing costs.

### Analysis
The biggest shifts in the analysis of data is within speed, volume and efficiency of processing, leading to quicker business insights. This is partly a result of both the technical advancements previously discussed. However it is also due to better understanding by businesses of the analytical techniques available. Furthermore, owing to the fact that less time and attention needs to be spent on hardware maintenance and ETL implementations more attention can be devoted to the analysis of data.

**what else needs to be said here?**

### Presentation
**TODO**

### Interaction
**TODO**

6 Current Business Landscape
----------------------------

### Big Data & Hadoop

>> “The world is one big data problem.” ~ Andrew McAfee

One attractive opportunity available to many companies is that of big data analytics. Big data is an opportunity for companies to get a competitive edge and to better understand customers. These opportunities are real and are a result of the ability for a business to consume vast amounts of data, which previously would have been an impossible task.

 >> "Big Data will spell the death of customer segmentation and force the marketer to understand each customer as an individual within 18 months or risk being left in the dust.” ~ Ginni Rometty, CEO, IBM

Whilst there is a certain degree of hype surrounding Big Data the excitement is owning to the fact that with very minimumal resources it is possible to get answers to previously unanswered questions. An average laptop computer is capable of processing tens of millions of data rows in seconds, a few servers on a distributed engine billions of rows. Considering there are only 8 billion people on the planet it is possible for a company of any size to ask a question of every single person on the planet and get an answer instantly.

>> “Without big data analytics, companies are blind and deaf, wandering out onto the web like deer on a freeway.” ~ Geoffrey Moore, author and consultant

Commonly Big Data is implemented using the Hadoop suite of tools, which has the backing of Yahoo!, Google and Apache Foundation. Whilst other big data tools are avilable the advantage of Hadoop is its open licensing model - effectively making it free software. Free as in cost, and free as in not tied down to a vendor. This effectively levels the playing field of the traditional database providers such as Oracle, SAP and IBM and is forcing those vendors to offer Hadoop not just as a value add-but as an alternative to proprietary systems.

Going with a Hadoop based system is usually the reference path, simply because of how the Hadoop suite has become the defacto indsutry standard. By choosing to adopt a Big Data or analytics platform which isn't at a minimum compatible with the main Hadoop components effictively means to become shut off from a vibrant growing ecosystem supported by vast numbers of talented developers, analysts and data scientists. Going back to our car analogy it would also be like running a road car on a combustible fuel that isn't available at the pump, whilst it is possible and may offer some attractive benefits for the vast majority of businesses this would make it's Big Data journey extremely challenging to say the least. Of course, following the trend isn't always the right thing to do.

*Figure 1. Hadoop stack defined*

### Open vs. Proprietary
Another of the choices faced by companies on their data science journey is whether to embrace open software and technology or adopt a proprietary stack. In the past whilst it has been tempting for companies to consider open-source software it has not always been entirely viable and few companies took the plunge. Datascience however offers a good opportunity to work with open technology across the complete stack including open-source software, open cloud technologies and software defined infrastructure. Common packages within the open data science stack include the Hadoop suite, R Stuido and Python as computational and analytical tools and visualisation and publishing tools commonly built around responsive layout display (D3.js).

>> Responsive:- content automatically fitting and self-tailoring layout suited to the screen size of the device displaying it.*

### Python & R
Another large software components used with modern data science armory is that of an open and versatile analytical engine built on statistics and mathematics but also encorporating general programming abilities, and designed to work directly with data rather than more generic programming objects. Python & R are popular choices (along with Scala and Java). The business the impact is that of a transition away from propritary statistical and analytical packages such as Excel, SPSS and IBM Rational. 

The choice of computational language is more subtle than evaulating and chosing one or another since the ultimate decision will likely depend on the aims of the business, its strategic objectives and which language has the best community support for the business's operating industry. Often a mix of languages is used and ultimaately the data science team will have a strong say in which tools they choose to adopt. The decision by the business should not be glossed over however as there are wider business implications.

Another important aspect of Python or R code is the ability for interactive worksheets to be created allowing the business consumers of data, e.g. the marketing manager, finance director or CEO to reproduce technically advanced computations and modify relevant parameters without the need to modify analytical models. These workbooks may be published as intranet or web assets, distributed about the business and built upon to enable collaboration between cross-functional teams.

[Python versus R adoption][3]

[3]:http://www.kdnuggets.com/2015/05/r-vs-python-data-science.html
**http://www.kdnuggets.com/wp-content/uploads/r-vs-python-numbers.jpg**

### Machine Learning
Any review of data science would not be complete without at least a cursory overview of machine learning and the impact on business. Machine learning (ML) is a discipline which incorporates scientific experimentation, statistical methods, programming and data feedback loops. Its name comes from the resultant ability of code to effectively learn through optimising decision algorithms. Large vendors such as Microsoft and IBM mpw offer cloud machine learning platforms for companies wishing to dip their toe in the ML ocean. These tools offer data scientists and analysts access to distributed compute as standard, graphic representations of algorithms &amp; workflows and access to proprietary R and Phyton libraries, as well as allowing extensible plugins.

>> "The big technology trend is to make systems intelligent and data is the raw material." ~ Amod Malviya, CTO at flipkart

The impact of machine learning on businesses is that complex data optimisations and simulations can be set up and run over time to form a constantly evolving analytical engine which naturally improves in perfomance. Examples of ML include the ability for a bank to detect with a defined level of confidence fraud transactions, or a medical provider the diagnosis of a specific disease within a patient, or a retailer to form an accurate predictive model of customer shopping behaviour.

7 Business Implications
-----------------------
The net business impact of everything we have discussed is sumarised in the table below. On one hand it is easy to capture and understand some of the benefits of modern data science translates e.g.cost savings, greater choice and better performance. However, on the other hand some of the benefits are less obvious, including the lower reliance on IT allowing for great focus on data consumption rather than administration. The table below represents the common benefits which can be realised by the majority of businesses, however this is not meant to be an exhaustive list. Other companies will find ways of leveraging modern data science and as the newer technologies are better understood by the industry as a whole, further benetifs are likely to emerge.

|Modern Data Science paradigm 		|Business Impact 						|
|-----------------------------------|---------------------------------------|
|Technology advances                |Realtime analytics, lower TCO			|
|Improved data science methodologies|Deeper analysis with greater bus. value|
|Open source                        |Greater choice, no vendor tie-in       |
|Machine Learning 					|Self optimising data analytics         |
|Big Data 							|360 insight, competitive advantage     |
|Cloud technology                   |Lower TCO, lower IT overhead           |
|R & Python                         |Reusable code, community support       |


8 Practical Applications
-------------------------

|Industry|Data Science use cases|
|--------|----------------------|
|Automotive|Auto sensors reporting vehicle location problems|
|Financial services|Risk, fraud detection, portfolio analysis, new product development|
|Manufacturing|Quality assurance, warranty analyses|
|Healthcare|Patient sensors, monitoring, electronic health records, quality of care|
|Oil and gas|Drilling exploration sensor analyses|
|Retail|Consumer sentiment analyses, optimized marketing, personalized targeting, market basket analysis, intelligent forecasting, inventory management|
|Utilities|Smart meter analyses for network capacity, smart grid|
|Law enforcement|Threat analysis, social media monitoring, photo analysis, trac optimization|
|Advertising|Customer targeting, location-based advertising, personalized retargeting, churn detection/prevention|

**EXPAND THIS SECTION**

*Vendor landscape / market share summary*
https://s3.amazonaws.com/files.dezyre.com/images/blog/Top+6+Hadoop+Vendors+providing+Best+in+Class+Big+Data+Solutions_2.PNG
3. http://siliconangle.com/files/2016/03/Top-Vendors-1080x675.png

9 Summary
---------

>> "Data is like teenage sex: everyone talks about it, nobody really knows how to do it, everyone thinks everyone else is doing it, so everyone claims they are doing it…" ~ Unknown Author

*Overview diagram of datascience landscape. Include DW/BI tools mentioned in this document*

>> "Data matures like wine, applications like fish." ~ James Governor, Founder RedMonk
