# Briefing — ANIM4LL

## Direção aprovada

Fotografia autoral em primeiro plano, clareza de apresentação, acabamento visual, acessibilidade e velocidade. Preservar a identidade escura, laranja como ação principal e verde como sinal discreto. Evitar efeitos e dependências sem necessidade.

## Escopo desta etapa

Home e uma página completa de apresentação de uma imagem de projeto. HTML e CSS estáticos, sem JavaScript ou build. Preservar as imagens originais e produzir derivados WebP responsivos. Não publicar em produção.

A home reaproveita o posicionamento existente: “presença com olhar” e organização de imagem, texto, WhatsApp e página. Contatos existentes: WhatsApp 5531933002072 e Instagram felipeaoc. “Movimento”, “Atmosfera” e “Assinatura” são títulos editoriais existentes, não nomes de clientes ou comprovação de trabalhos contratados.

## Conteúdo e seleção

Home: pôr do sol, esporte, guitarrista, universo e cantor. Projeto inicial: “Atmosfera”, com portfolio-guitarrista.jpg, apresentado como seleção visual disponível. Não relacionar olhar-cantor.jpg ao mesmo evento ou projeto sem confirmação. Não atribuir autoria ou resultados com base apenas no nome dos arquivos.

## Pendências editoriais

- Confirmar autoria, créditos e contexto de cada imagem.
- Primeiro projeto: nome definitivo, artista/evento, data, local, objetivo, participação de Felipe, processo, entregas e imagens adicionais relacionadas. A página identifica essa ausência explicitamente.
- Confirmar escopo das atividades “imagem, texto, WhatsApp e página”. O “Raio-X” existente não ganha promessa ou pacote sem detalhamento confirmado.
- Confirmar telefone, perfil e texto final de apresentação antes de publicar.
- Definir domínio e imagem de compartilhamento; URL canônica depende do endereço definitivo.
- Clientes, depoimentos, preços e resultados não estão documentados e não serão inventados.

## Critérios de aceitação

Navegação móvel disponível; conteúdo acessível sem JavaScript; títulos sem versão técnica; imagens com alternativas e dimensões; foco visível; link para pular ao conteúdo; movimento reduzido respeitado; links e imagens locais íntegros; avaliação em 360, 390, 768 e 1440 pixels, zoom e teclado.

## Execução

Na raiz do checkout, execute `python3 -m http.server 8000 --bind 0.0.0.0`.
Home: `/`; projeto: `/projeto-atmosfera.html`. Não há comando de build: os arquivos são os próprios artefatos de entrega. Testar HTTP e navegador antes de publicar.

## Próximas etapas

1. Revisar home e página de projeto desta entrega.
2. Completar o projeto com informações verificadas e galeria relacionada.
3. Refinar após revisão editorial, preparar metadados definitivos e publicar somente com autorização.

## Validação desta entrega

- Chromium/Playwright: ambas as páginas em 360, 390, 768 e 1440 px, sem transbordamento horizontal; imagens carregadas e menu disponível.
- Teclado: link inicial para pular ao conteúdo; foco visível definido no CSS. Movimento reduzido e ampliação de texto de 200% verificados.
- Links locais e âncoras: respostas HTTP 200 e destinos existentes. Links externos: URLs HTTPS de WhatsApp e Instagram conferidas; envio de mensagens e disponibilidade das plataformas não testados.
- axe-core: nenhuma violação nas regras WCAG 2 A/AA e 2.1 AA avaliadas, em 390 e 1440 px nas duas páginas. Não substitui avaliação humana com leitor de tela.
- Capturas de home em celular/desktop e projeto em desktop revisadas visualmente.
- Build não aplicável: HTML, CSS e imagens são servidos diretamente. Nenhuma dependência de aplicação adicionada; ferramentas de auditoria instaladas somente em /tmp.
- Produção não publicada. Originais preservados.

## Aperfeiçoamento após revisão

- A fotografia de abertura mantém o enquadramento horizontal; hierarquia, espaçamentos e detalhes de verde fluorescente refinados.
- O cartão Atmosfera inteiro abre a página, com nome acessível único. Imagens do portfólio usam `sizes` correspondente às três colunas.
- Contatos existentes apresentados de forma explícita; o link Contato aponta à seção da própria página.
- Pendências de Atmosfera continuam públicas em um painel de documentação, com lista expansível sem JavaScript. Autoria e contexto continuam pendentes.
- Metadados de título, descrição, idioma e cor do navegador adicionados. Domínio, URL canônica e imagem de compartilhamento permanecem pendentes.
- Verificação adicional: telas de 320 a 1440 px, texto em 200% nas duas páginas, abertura do cartão pela foto, painel de pendências por teclado e retorno à home.
- Verificação reproduzível sem dependências: `python3 scripts/check_site.py`. Confere páginas, recursos locais, referências relativas, âncoras, IDs, idioma, títulos e atributos de imagem. Não é build nem certificação de acessibilidade.
- ZIP e quatro capturas atualizados em `entrega/`. Não há anexo para download nesta interface; a entrega está preparada para revisão no GitHub pela branch revisao-home-atmosfera, sem publicação em produção. A política do navegador bloqueia a validação por `file://`; teste em Chrome no Mac permanece pendente.
