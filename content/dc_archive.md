---
layout: page
title: Archiwium DataCommunity
permalink: /dc_archive/
feature-img: "assets/img/pexels/circuit.jpeg"
archive_videos:
    - title: "Patryk Miziuła, Uczenie maszynowe – jak zacząć (meetup 37)"
      url: "7bU_4QBubGA"
    - title: "Grzegorz Łoś - Maszynowe rozpoznawanie obrazów w praktyce (meetup 38)"
      url: "01eA1VwWXzs"
    - title:   "Andrzej Pyskir - Czy można nauczyć komputer znajdować budynki na zdjęciach satelitarnych? (meetup 40)"
      url: "v-PJ9xq5lhw"
    - title:   "Błażej Osiński Reinforcement learning - czy komputer da się uczyć metodą kija i marchewki? (meetup 41)"
      url: "TP_Gc5ik80Y"
    - title:   "Artur Zygadło - Wprowadzenie do przetwarzania języka naturalnego (NLP) (meetup 44)"
      url: "IUbFMt_4_Hw"
    - title:   "Paulina Knut - Renowacja filmu z AI (meetup 45)"
      url: "yPGhF6Z1Xgg"
    - title:   "Michał Woś- Rozpoznawanie tekstu z ustrukturyzowanych dokumentów (meetup 47)"
      url: "LqghaxDEJTg"
tags: [About, Archive]
---

Przed powstaniem PyData Bydgoszcz, współpracowaliśmy ze społecznością DataCommunity - nagrania dotyczące tematyki
uczenia maszynowego i AI możesz obejrzeć poniżej

{% for video in page.archive_videos %}
## {{ video.title }}
<iframe width="560" height="315" src="https://www.youtube.com/embed/{{ video.url }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
{% endfor %}