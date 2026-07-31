---
bookCollapseSection: true
title: "Development History"
weight: 60
---

# Development History

Note that while the explanation provided here overlaps in part with what is stated in the paper by Shōju Ikeda, Liu Guanwei, Jung Munho, Zhang Xinfang, and Li Yuan, “Full-text Database of *Ruijū Myōgishō*, Kanchi-in MS : A Look at Development Methods and Calculating the Number of Headwords." (*Kuntengo to Kuten Shiryō* 144, 2020), it has been completely overhauled and rewritten by the first author, Ikeda, who organized the terminology and substantially added subsequent research findings.

## Database Construction Process

The *Ruijū Myōgishō* of the Kanchi-in manuscript is an old handwritten manuscript, and because it contains an extremely large number of difficult characters, we proceeded with database construction using the following steps.

**Step 1:** Scan the facsimile edition and cut out each listed character to create an image database of the *Ruijū Myōgishō* of the Kanchi-in manuscript. The image files of the listed characters are named according to the location of the listed character. This image file name will later be used as the listed character ID.


**Step 2:** Add the location information to the existing *Tenrei Banshō Meigi* database by referring to the "Kanji Index" included in Masamune Atsuo's *Ruijū Myōgishō, Volume 2* (Kazama Shobō, 1955). Input the location information from the "Kanji Index" into the *Tenrei Banshō Meigi* data rearranged in the order of the *Dai Kanwa Jiten* index numbers compiled by Morohashi Tetsuji. Then, rearrange it according to the order of locations in the Kanchi-in manuscript, collate it with the text of the Kanchi-in manuscript, and add the page numbers and character order of the Kanchi-in manuscript that are not found in the "Kanji Index."

**Step 3:** Take in various information included in the *Tenrei Banshō Meigi* database (*Dai Kanwa Jiten* index numbers, Unicode numbers, kanji characters, location information in the *Tenrei Banshō Meigi*) and the corresponding location information of the *Ruijū Myōgishō* Kanchi-in manuscript created in Step 2, into the *Ruijū Myōgishō* Kanchi-in manuscript image database (created in Step 1) to create an input database for the *Ruijū Myōgishō* Kanchi-in manuscript text.

**Step 4:** While referring to the facsimile edition of the *Ruijū Myōgishō* Kanchi-in manuscript (Tenri Library Rare Books Series, Japanese Books Section, Volumes 32-34) and the *Ruijū Myōgishō* Kanchi-in manuscript image database, add the text information for the listed characters and their explanations ("chūmon/chūbun") to the input database for the *Ruijū Myōgishō* Kanchi-in manuscript text created in Step 3.

**Step 5:** Integrate the *Ruijū Myōgishō* Kanchi-in manuscript image database and the *Ruijū Myōgishō* Kanchi-in manuscript text database to form the *Ruijū Myōgishō* Kanchi-in manuscript database. Then, check and revise the text content using the newly published color facsimile edition of the *Ruijū Myōgishō* Kanchi-in manuscript (New Tenri Library Rare Books Series, Volumes 9-11). When checking the text content, also distinguish between compound word entries and variant character entries in the listed items, and distinguish between font annotations, pronunciation annotations, meaning annotations, and Japanese glosses in the explanations, and add this information.

**Step 6:** Publish the completed *Ruijū Myōgishō* Kanchi-in manuscript database on the internet and provide a search service.

## Online Information Provision

HDIC's online information provision consists of three parts: the main site, the search screen, and the text data. The main site is available at the following URL and summarizes the overview of the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC) (in Japanese, Chinese, and English), a list of research results, links to related sites, etc.
[https://hdic.jp](https://hdic.jp)

The search screen is available at the following URL, where you can use the HDIC Viewer to search the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC). The HDIC Viewer is maintained and managed by [Liu Guanwei](https://researchmap.jp/liuguanwei?lang=en) and allows searches not only on personal computers but also on smartphones.
[https://viewer.hdic.jp](https://viewer.hdic.jp)

We would like to express our gratitude to [Tomohiko Morioka](https://researchmap.jp/morioka-tomohiko?lang=en) for his technical support in maintaining and managing the hdic.jp website.

The text data created by the Integrated Database of Hanzi Dictionaries in Early Japan (HDIC) is available at [https://github.com/shikeda/HDIC](https://github.com/shikeda/HDIC), which preserves records of data revisions and provides the latest versions of the full-text databases for the Song Dynasty edition of the *Yupian*, the Kōzan-ji manuscript of the *Tenrei Banshō Meigi*, and the Tenji manuscript of the *Shinsen Jikyō*.

The KRM data specifically underwent a specification change in March 2025, and its current full-text database is published separately at [https://github.com/shikeda/krm](https://github.com/shikeda/krm) (see [Resource Documented](/en/docs/krm/#resource-documented) for the current version and citation).

Please note that the above URLs are subject to change in the future. Maintaining and managing the constructed data is a significant challenge.
