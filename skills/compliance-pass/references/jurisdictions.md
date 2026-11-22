# National Jurisdiction Packs

Read the active pack(s) named in `compliance.json` `jurisdictions` during
Movement 3 (`audit`) and Movement 4 (`draft`). GDPR is a regulation with
national derogations, while contract, e-commerce, liability, and consumer rules
are governed directly by the company's home Member State law (and mandatory
consumer law of the buyer's residence).

---

## Pack `pt`: Portugal (Lisbon / Portuguese Company)

Applies when the provider is established in Portugal (for example a *Sociedade
por Quotas, Lda.* or *Sociedade Anónima, S.A.* with *sede* in Lisbon).

### 1. Mandatory Corporate Disclosures (*DL n.º 7/2004*, Art. 10.º & *Código das Sociedades Comerciais*, Art. 171.º)

Every Portuguese online service provider must make permanently and easily
accessible (in Terms of Service and Privacy Policy):
- **Denominação social** (full legal company name, including *Lda.*, *Unipessoal
  Lda.*, or *S.A.*).
- **Sede social** (full registered street address in Portugal).
- **NIPC** (*Número de Identificação de Pessoa Coletiva* / VAT number `PT...`)
  and commercial registry details (*Conservatória do Registo Comercial*).
- **Capital social** (share capital, mandatory on external corporate documents
  and electronic pages under Art. 171.º CSC for *Lda.* / *S.A.*).
- **Direct electronic contact** (email address for rapid, direct communication).

If any of these five fields is missing from `business/entity.md`, raise a
blocking `clarify` item in `decisions/` before drafting `documents/`.

### 2. Portuguese Data Protection Specifics (*Lei n.º 58/2019* & *Lei n.º 41/2004*)

- **Supervisory Authority:** Name the **Comissão Nacional de Proteção de Dados
  (CNPD)**, Av. D. Carlos I, 134 - 1.º, 1200-651 Lisboa, Portugal
  (`https://www.cnpd.pt`), alongside the right to contact another EEA authority.
- **Age of Digital Consent (Art. 16.º Lei n.º 58/2019):** 13 years in Portugal
  for information society services based on consent, **however** SaaS contracts
  require legal contracting capacity (18+ under Portuguese *Código Civil*, Art.
  122.º/130.º). Set minimum age in ToS and Privacy Policy to **18 years** unless
  the user explicitly directs otherwise.
- **Deceased Persons' Data (Art. 17.º Lei n.º 58/2019):** Portuguese law
  protects certain personal data rights post-mortem, exercisable by designated
  persons or heirs unless the data subject prohibited it. Acknowledge applicable
  statutory rights under *Lei n.º 58/2019* concisely in User Rights.
- **Tax & Accounting Retention (*CIRC* Art. 123.º / *CIVA*):** Invoices, billing
  records, and accounting documents must be archived for **10 calendar years**
  under Portuguese tax law (`Art. 6(1)(c)` GDPR legal obligation). Never promise
  immediate deletion of billing/invoice records upon account deletion; carve out
  the 10-year statutory archive explicitly.
- **Electronic Communications & Direct Marketing (*Lei n.º 41/2004*, Art.
  13.º-A):** Marketing emails to individuals require prior consent, with soft
  opt-in permitted only for existing customers regarding similar own products/
  services if given a clear, free opt-out at collection and in every message.

### 3. Portuguese Contract & Liability Rules (*Código Civil* & *DL n.º 446/85* LCCG)

- **No Waiver of *Dolo* or *Culpa Grave* (*Art. 809.º do Código Civil* & *Art.
  18.º(a)-(d) LCCG*):** Under Portuguese law, any clause excluding or capping
  liability in advance for willful misconduct (*dolo*), gross negligence (*culpa
  grave*), or death/personal injury is **null and void**.
  - **Drafting rule:** Always write the ToS Limitation of Liability clause with
    an explicit carve-out: *"Nothing in these Terms excludes or limits liability
    for willful misconduct (dolo), gross negligence (culpa grave), death or
    personal injury, or any other liability that cannot be excluded under
    applicable Portuguese or EU law."* Subject to that carve-out, cap aggregate
    liability for ordinary negligence (*mera culpa* / *culpa leve*) to fees paid
    in the preceding 12 months.
- **Standard Contract Terms (*Cláusulas Contratuais Gerais*, DL n.º 446/85):**
  Avoid unilateral right to change prices or material terms without prior
  reasonable notice (for example 30 days' advance email notice) and the
  customer's right to cancel before the change takes effect (*Art. 22.º LCCG*).
- **Governing Law & Forum:** Governing law is the **law of the Portuguese
  Republic**. For **Business Customers**, exclusive jurisdiction is the courts
  of the **Comarca de Lisboa**, Portugal.

### 4. Dual-Track Consumer Rules (`customer_model: "b2b_and_consumers"`)

When individual consumers (*consumidores* acting outside a trade, business, or
profession under *Lei n.º 24/96*) are permitted to subscribe alongside
businesses, include a dedicated **Consumer Provisions** section in the Terms of
Service covering four mandatory Portuguese/EU protections:

1. **14-Day Right of Withdrawal (*Direito de Livre Resolução*, DL n.º 24/2014,
   Art. 10.º & Art. 17.º):**
   - Consumers purchasing online have **14 days** from contract conclusion to
     withdraw without giving any reason and without penalty, by emailing the
     contact address (or using a clear cancellation/withdrawal statement).
   - **Digital service / immediate execution nuance:** For ongoing digital SaaS
     services (*prestação de serviços*), if the consumer requests immediate
     provisioning during the 14-day period, withdrawal remains available within
     14 days (unless fully performed under statutory exceptions), subject to
     proportional payment for services used up to withdrawal if expressly
     requested (*Art. 15.º DL n.º 24/2014*); for one-off digital content/credits
     supplied immediately (such as instant usage boosts), loss of withdrawal
     under *Art. 17.º(1)(l)* applies **only** if the checkout collects prior
     express consent and acknowledgment + confirmation on a durable medium. Flag
     checkout consent checkbox alignment in `review.md` / `decisions/`!
2. **Conformity of Digital Services (*DL n.º 84/2021*):**
   Consumers benefit from statutory remedies for lack of conformity of digital
   services throughout the subscription period (repair/bringing into conformity,
   proportional price reduction, or contract termination), plus necessary
   security and functional updates.
3. **Alternative Dispute Resolution, RAL (*Lei n.º 144/2015*, Art. 18.º):**
   Mandatory disclosure of the competent Portuguese consumer arbitration center
   for Lisbon-headquartered providers (and general national portal):
   - **Centro de Arbitragem de Conflitos de Consumo de Lisboa (CACCL):** Rua
     dos Douradores, n.º 116, 2.º, 1100-207 Lisboa (`http://www.centroarbitragemlisboa.pt`)
   - **CNIACC (Centro Nacional de Informação e Arbitragem de Conflitos de
     Consumo)** (`https://www.cniacc.pt`, for consumers outside regional center
     coverage) and official portal `https://www.consumidor.gov.pt`.
   *(Note: The old EU ODR platform `ec.europa.eu/consumers/odr` was discontinued
   in July 2025 under Regulation (EU) 2024/3228. **Never** link to the defunct
   EU ODR platform!)*
4. **Electronic Complaints Book (*Livro de Reclamações Eletrónico*, DL n.º
   156/2005):**
   Portuguese suppliers providing goods or services online to consumers must
   register on and link to the **Livro de Reclamações Eletrónico**
   (`https://www.livroreclamacoes.pt`). Reference it in Consumer Provisions and
   flag footer badge/registration readiness in `review.md` if not yet on the
   website.
5. **Mandatory Consumer Forum:** Clarify that the *Comarca de Lisboa* exclusive
   jurisdiction clause applies to Business Customers and never deprives a
   consumer of mandatory statutory court jurisdiction of their domicile (EU
   Regulation 1215/2012, Art. 18).

---

## Optional Add-on Notes (`uk-gdpr`, `us-ccpa`)

Include only when the user explicitly adds `uk-gdpr` or `us-ccpa` to
`jurisdictions`:
- **`uk-gdpr`:** Reference UK GDPR + Data Protection Act 2018, ICO
  (`https://ico.org.uk`) as UK supervisory authority, and UK International Data
  Transfer Addendum (IDTA) alongside EU SCCs.
- **`us-ccpa`:** State explicitly in Privacy Policy that the company **does not
  sell or share personal information** for cross-context behavioral advertising
  as defined under CCPA/CPRA, and honor access/deletion/non-discrimination
  rights.
