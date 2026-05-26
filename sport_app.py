import streamlit as st
from dataclasses import dataclass
from typing import List
from datetime import datetime

st.set_page_config(
    page_title="Sport App UAE — Python MVP",
    page_icon="🏝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@dataclass
class Person:
    name: str
    role: str
    location: str
    sports: List[str]
    interests: List[str]
    vibe: str
    score: int

@dataclass
class Circle:
    name: str
    category: str
    description: str
    members: int
    access: str

@dataclass
class Event:
    name: str
    category: str
    location: str
    time: str
    description: str
    price: str
    capacity: int
    sponsor_ready: bool

@dataclass
class BrandCollab:
    brand: str
    category: str
    title: str
    description: str
    benefit: str
    activation: str
    partner_level: str

PEOPLE = [
    Person("Ahmed", "Investor", "Downtown", ["Football", "Padel"], ["Founders", "Finance", "Networking"], "High-signal", 94),
    Person("Lina", "Wellness Trainer", "Jumeirah", ["Yoga", "Running"], ["Wellness", "Brand events"], "Community builder", 88),
    Person("Mark", "Startup Founder", "Dubai Marina", ["Padel", "Gym"], ["Startups", "AI", "Networking"], "Founder energy", 91),
    Person("Noura", "Brand Manager", "Business Bay", ["Running", "Yoga"], ["Sportswear", "Creators", "Events"], "Brand connector", 86),
    Person("Dmitry", "Real Estate Broker", "Palm Jumeirah", ["Tennis", "Padel"], ["Luxury", "Investors", "Networking"], "Premium circle", 82),
]

CIRCLES = [
    Circle("Founders Padel", "Business + Sport", "Invite-only padel circle for founders, investors and operators.", 128, "Apply"),
    Circle("Marina Morning Club", "Wellness", "Morning run, coffee, recovery and real introductions before work.", 342, "Join"),
    Circle("Private Tennis Network", "Premium Sport", "Verified players, private courts and high-signal social matches.", 74, "Request"),
    Circle("Wellness Creators UAE", "Brands + Influencers", "Trainers, creators and brands building wellness activations.", 212, "Join"),
]

EVENTS = [
    Event("Founder Padel Night", "Business networking", "Dubai Marina", "Tonight · 20:30", "Private game for founders, operators and investors. Small group, no random crowd.", "AED 75", 8, True),
    Event("Creator Run x Wellness Breakfast", "Brand collaboration", "Jumeirah Beach", "Saturday · 07:30", "Run, coffee, content, wellness partners and curated introductions.", "AED 95", 80, True),
    Event("Expat Integration Through Sport", "Social impact", "Downtown Dubai", "Next Thursday · 18:00", "Community event aligned with UAE healthy lifestyle and social inclusion narrative.", "Free", 150, True),
    Event("Gym Buddy Match Night", "Fitness social", "Business Bay", "Tomorrow · 19:00", "AI-matched gym partners by goals, level and preferred training style.", "AED 45", 30, False),
]

BRAND_COLLABS = [
    BrandCollab(
        "Nike",
        "Sportswear",
        "Nike Run Club Dubai",
        "Серия закрытых утренних забегов для активного русскоязычного и international community UAE.",
        "20% discount + early access drops",
        "Weekly run + creator content + branded challenge",
        "Official Partner"
    ),
    BrandCollab(
        "HEAD",
        "Padel / Tennis",
        "HEAD Padel Nights",
        "Падел-вечера с тест-драйвом ракеток, мини-турнирами, призами и нетворкингом.",
        "Free racket test + tournament prizes",
        "Padel tournament + equipment demo + content production",
        "Equipment Partner"
    ),
    BrandCollab(
        "Red Bull",
        "Energy / Events",
        "Red Bull Founder Game Night",
        "Энергичный вечер: падел, музыка, нетворкинг, подарки и afterparty.",
        "Free drinks + VIP access",
        "Sport event + music + founder networking",
        "Energy Partner"
    ),
    BrandCollab(
        "Warehouse Gym",
        "Fitness Club",
        "Premium Training Session",
        "Закрытая тренировка для участников приложения, амбассадоров и новых premium members.",
        "Free first class",
        "Community workout + membership upsell",
        "Gym Partner"
    ),
    BrandCollab(
        "Seven Wellness",
        "Recovery / Wellness",
        "Recovery & Ice Bath Club",
        "Восстановление, ice bath, breathwork и soft networking после тренировок.",
        "25% discount for members",
        "Wellness session + community recovery ritual",
        "Wellness Partner"
    ),
]

SPORTS = ["Padel", "Football", "Tennis", "Running", "Yoga", "Gym"]
GOALS = ["New friends", "Business networking", "Premium circles", "Wellness lifestyle", "Founder community"]
LOCATIONS = ["Dubai Marina", "Downtown", "Jumeirah", "Business Bay", "Palm Jumeirah"]

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "Alex",
        "location": "Dubai Marina",
        "sports": ["Padel", "Gym"],
        "goals": ["Business networking", "Founder community"],
        "level": "Intermediate",
        "premium": False
    }

for key in ["joined_events", "joined_circles", "connections", "intro_requests", "saved_offers", "brand_activations"]:
    if key not in st.session_state:
        st.session_state[key] = []

if "notifications" not in st.session_state:
    st.session_state.notifications = [
        "AI found 3 strong matches for your UAE social circle.",
        "Founder Padel Night has 2 people from your target network.",
        "Nike Run Club Dubai is available for your profile."
    ]

def navigate(page: str):
    st.session_state.page = page
    st.rerun()

def match_score(person: Person) -> int:
    user_sports = set(st.session_state.profile["sports"])
    user_goals = set(st.session_state.profile["goals"])
    score = person.score
    score += len(user_sports.intersection(set(person.sports))) * 4
    score += len(user_goals.intersection(set(person.interests))) * 3
    if person.location == st.session_state.profile["location"]:
        score += 5
    return min(score, 99)

def notify(text: str):
    st.success(text)
    st.session_state.notifications.insert(0, text)

def metric_card(label, value, help_text=None):
    st.metric(label, value, help=help_text)

def divider():
    st.markdown("<div class='soft-divider'></div>", unsafe_allow_html=True)

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
}
.stApp {
    background:
      radial-gradient(circle at top left, rgba(199,255,90,.18), transparent 28%),
      radial-gradient(circle at bottom right, rgba(120,205,255,.18), transparent 28%),
      #f7f6f1;
    color: #111315;
}
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(17,19,21,.08);
}
h1, h2, h3 {
    letter-spacing: -0.045em;
}
.hero {
    background: linear-gradient(135deg, #111315, #22292f);
    color: white;
    padding: 38px;
    border-radius: 34px;
    min-height: 330px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    box-shadow: 0 30px 80px rgba(17,19,21,.18);
    position: relative;
    overflow: hidden;
}
.hero:before {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    border-radius: 999px;
    background: radial-gradient(circle, #c7ff5a, transparent 68%);
    right: -80px;
    top: -90px;
    opacity: .9;
}
.hero h1 {
    font-size: 58px;
    line-height: .95;
    margin-bottom: 12px;
    position: relative;
}
.hero p {
    color: rgba(255,255,255,.68);
    font-size: 18px;
    max-width: 620px;
    position: relative;
}
.card {
    background: rgba(255,255,255,.76);
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 14px 46px rgba(17,19,21,.06);
}
.dark-card {
    background: #111315;
    color: white;
    border-radius: 28px;
    padding: 24px;
    box-shadow: 0 18px 60px rgba(17,19,21,.18);
}
.dark-card p {
    color: rgba(255,255,255,.68);
}
.tag {
    display:inline-block;
    padding: 7px 11px;
    background:#eef3e2;
    border-radius:999px;
    color:#4a5237;
    font-size:12px;
    font-weight:800;
    margin: 0 6px 6px 0;
}
.premium-tag {
    display:inline-block;
    padding: 7px 11px;
    background:#c7ff5a;
    border-radius:999px;
    color:#111315;
    font-size:12px;
    font-weight:900;
    margin-bottom: 8px;
}
.brand-card {
    background: linear-gradient(145deg, rgba(255,255,255,.84), rgba(240,243,235,.78));
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 30px;
    padding: 26px;
    box-shadow: 0 18px 56px rgba(17,19,21,.07);
}
.brand-hero {
    background: linear-gradient(135deg, #111315, #20262c);
    color: white;
    border-radius: 34px;
    padding: 34px;
    box-shadow: 0 24px 70px rgba(17,19,21,.2);
}
.brand-hero p {
    color: rgba(255,255,255,.68);
}
.soft-divider {
    height: 1px;
    background: rgba(17,19,21,.08);
    margin: 24px 0;
}
.small-muted {
    color:#73777d;
    font-size: 14px;
}
.match-score {
    display:inline-block;
    background:#c7ff5a;
    color:#111315;
    border-radius:999px;
    padding:7px 12px;
    font-weight:900;
    font-size:13px;
}
.stButton > button {
    border-radius: 18px;
    border: 0;
    font-weight: 800;
    min-height: 46px;
}
[data-testid="stMetric"] {
    background: rgba(255,255,255,.7);
    padding: 18px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.85);
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## Sport App UAE")
    st.caption("Social OS for expats in UAE")
    st.write("")

    pages = [
        "Home",
        "Onboarding",
        "AI Matches",
        "Circles",
        "Events",
        "Brand Collabs",
        "People",
        "Map",
        "Profile",
        "Business",
        "Admin"
    ]

    for page_name in pages:
        if st.button(page_name, use_container_width=True, type="primary" if st.session_state.page == page_name else "secondary"):
            navigate(page_name)

    divider()
    st.markdown("### Notifications")
    for note in st.session_state.notifications[:4]:
        st.caption("• " + note)

    divider()
    st.markdown("### MVP state")
    st.caption(f"Events joined: {len(st.session_state.joined_events)}")
    st.caption(f"Circles joined: {len(st.session_state.joined_circles)}")
    st.caption(f"Connections: {len(st.session_state.connections)}")
    st.caption(f"AI intro requests: {len(st.session_state.intro_requests)}")
    st.caption(f"Saved brand offers: {len(st.session_state.saved_offers)}")

page = st.session_state.page

if page == "Home":
    st.markdown("""
    <div class="hero">
      <h1>Your social life in UAE starts here.</h1>
      <p>Meet the right people through sport, wellness and curated real-world communities. Not a sports booking app — a social operating system for expats.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1:
        metric_card("Core pain", "No circle", "New city, random chats, no trusted social path.")
    with c2:
        metric_card("Core hook", "Belonging", "Meet people through activity, not awkward coffee chats.")
    with c3:
        metric_card("Main loop", "Invites", "AI intros, circles, events, status and momentum.")

    st.write("")
    left, right = st.columns([1.2, .8])
    with left:
        st.markdown("### Tonight for you")
        event = EVENTS[0]
        st.markdown(f"""
        <div class="dark-card">
          <span class="premium-tag">94% fit · AI recommended</span>
          <h2>{event.name}</h2>
          <p>{event.description}</p>
          <p><b>{event.time}</b> · {event.location} · {event.price}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Request invite", use_container_width=True, type="primary"):
            if event.name not in st.session_state.joined_events:
                st.session_state.joined_events.append(event.name)
            notify(f"Invite requested for {event.name}")

    with right:
        st.markdown("### Featured collab")
        collab = BRAND_COLLABS[0]
        st.markdown(f"""
        <div class="card">
          <span class="tag">{collab.partner_level}</span>
          <h3>{collab.title}</h3>
          <p><b>{collab.brand}</b></p>
          <p>{collab.description}</p>
          <p class="small-muted">{collab.benefit}</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View brand collabs", use_container_width=True):
            navigate("Brand Collabs")

elif page == "Onboarding":
    st.markdown("## Build your UAE social graph")
    st.caption("This onboarding controls match quality, circles and event recommendations.")

    with st.form("profile_form"):
        name = st.text_input("Name", st.session_state.profile["name"])
        location = st.selectbox("Main area", LOCATIONS, index=LOCATIONS.index(st.session_state.profile["location"]))
        sports = st.multiselect("Sports you actually do", SPORTS, default=st.session_state.profile["sports"])
        goals = st.multiselect("What are you looking for?", GOALS, default=st.session_state.profile["goals"])
        level = st.select_slider("Sport level", ["Beginner", "Intermediate", "Advanced", "Semi-pro"], value=st.session_state.profile["level"])

        submitted = st.form_submit_button("Save and generate matches", use_container_width=True, type="primary")
        if submitted:
            st.session_state.profile.update({
                "name": name,
                "location": location,
                "sports": sports,
                "goals": goals,
                "level": level
            })
            notify("Profile updated. AI matches regenerated.")
            navigate("AI Matches")

elif page == "AI Matches":
    st.markdown("## AI Matches")
    st.caption("Mock AI logic: matches by sports, goals, location and networking intent.")

    sorted_people = sorted(PEOPLE, key=match_score, reverse=True)

    for person in sorted_people:
        score = match_score(person)
        st.markdown(f"""
        <div class="card">
          <div style="display:flex;justify-content:space-between;align-items:center;gap:16px;">
            <div>
              <h3>{person.name} · {person.role}</h3>
              <p class="small-muted">{person.location} · {person.vibe}</p>
            </div>
            <span class="match-score">{score}% fit</span>
          </div>
          <p style="margin-top:12px;">Why connect: shared interests in {", ".join(person.interests[:2])} and activities around {", ".join(person.sports[:2])}.</p>
        </div>
        """, unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button(f"Connect with {person.name}", key=f"connect_{person.name}", use_container_width=True):
                if person.name not in st.session_state.connections:
                    st.session_state.connections.append(person.name)
                notify(f"Connection request sent to {person.name}")
        with b2:
            if st.button("Ask AI for intro", key=f"intro_{person.name}", use_container_width=True):
                if person.name not in st.session_state.intro_requests:
                    st.session_state.intro_requests.append(person.name)
                notify(f"AI intro request created for {person.name}")
        with b3:
            if st.button("Suggest event", key=f"event_{person.name}", use_container_width=True):
                notify(f"Suggested Founder Padel Night with {person.name}")
        divider()

elif page == "Circles":
    st.markdown("## Curated circles")
    st.caption("The core moat: communities, identity and social lock-in.")

    for circle in CIRCLES:
        st.markdown(f"""
        <div class="card">
          <span class="tag">{circle.category}</span>
          <h3>{circle.name}</h3>
          <p>{circle.description}</p>
          <p class="small-muted">{circle.members} members · {circle.access}</p>
        </div>
        """, unsafe_allow_html=True)
        c1, c2 = st.columns([1,1])
        with c1:
            if st.button(f"{circle.access}: {circle.name}", key=f"circle_{circle.name}", use_container_width=True, type="primary"):
                if circle.name not in st.session_state.joined_circles:
                    st.session_state.joined_circles.append(circle.name)
                notify(f"{circle.access} sent for {circle.name}")
        with c2:
            if st.button("See members", key=f"members_{circle.name}", use_container_width=True):
                notify(f"Showing high-signal members of {circle.name}")
        divider()

elif page == "Events":
    st.markdown("## Events")
    st.caption("Offline-to-online loop: users meet in real life and return to app for follow-up, status and new invites.")

    category = st.selectbox("Filter", ["All", "Business networking", "Brand collaboration", "Social impact", "Fitness social"])
    filtered = [e for e in EVENTS if category == "All" or e.category == category]

    for event in filtered:
        sponsor = "Sponsor-ready" if event.sponsor_ready else "Community event"
        st.markdown(f"""
        <div class="card">
          <span class="tag">{event.category}</span><span class="tag">{sponsor}</span>
          <h3>{event.name}</h3>
          <p>{event.description}</p>
          <p class="small-muted">{event.time} · {event.location} · {event.price} · Capacity {event.capacity}</p>
        </div>
        """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("Join / request invite", key=f"join_{event.name}", use_container_width=True, type="primary"):
                if event.name not in st.session_state.joined_events:
                    st.session_state.joined_events.append(event.name)
                notify(f"Joined / requested: {event.name}")
        with c2:
            if st.button("Share with circle", key=f"share_{event.name}", use_container_width=True):
                notify(f"Shared {event.name} with your circle")
        with c3:
            if st.button("Brand proposal", key=f"brand_{event.name}", use_container_width=True):
                notify(f"Generated sponsor angle for {event.name}")
        divider()

elif page == "Brand Collabs":
    st.markdown("## Brand collaborations")
    st.caption("Бренды становятся частью комьюнити: события, скидки, челленджи, амбассадоры и доступ к активной аудитории UAE.")

    st.markdown("""
    <div class="brand-hero">
      <span class="premium-tag">Partner ecosystem</span>
      <h1>Not ads. Experiences.</h1>
      <p>Мы не продаём баннеры. Мы создаём события, где бренд становится частью lifestyle, спорта, нетворкинга и живого комьюнити.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Brand revenue", "High margin", "Sponsorship + activation fees")
    with c2:
        metric_card("User value", "Offers", "Discounts, early access, gifts")
    with c3:
        metric_card("Community value", "Events", "Real-world engagement")
    with c4:
        metric_card("Partner value", "Audience", "Premium expats and founders")

    st.write("")

    for collab in BRAND_COLLABS:
        st.markdown(f"""
        <div class="brand-card">
          <span class="tag">{collab.category}</span>
          <span class="tag">{collab.partner_level}</span>
          <h2>{collab.title}</h2>
          <p><b>{collab.brand}</b></p>
          <p>{collab.description}</p>
          <p class="small-muted"><b>Benefit for users:</b> {collab.benefit}</p>
          <p class="small-muted"><b>Activation:</b> {collab.activation}</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button(f"Join {collab.brand} activation", key=f"join_brand_{collab.brand}", use_container_width=True, type="primary"):
                if collab.title not in st.session_state.brand_activations:
                    st.session_state.brand_activations.append(collab.title)
                notify(f"You joined {collab.title}")

        with c2:
            if st.button("Save offer", key=f"save_brand_{collab.brand}", use_container_width=True):
                if collab.brand not in st.session_state.saved_offers:
                    st.session_state.saved_offers.append(collab.brand)
                notify(f"{collab.brand} offer saved to your profile")

        with c3:
            if st.button("Share with circle", key=f"share_brand_{collab.brand}", use_container_width=True):
                notify(f"{collab.title} shared with your circle")

        divider()

    st.markdown("## For brands")
    st.markdown("""
    <div class="card">
      <h3>Why brands care</h3>
      <p>Sport App UAE даёт брендам не просто показы, а доступ к живому комьюнити: founders, expats, premium lifestyle audience, wellness people and creators.</p>
      <p class="small-muted">Monetization: sponsorship fee, CPA, event budget, promoted circles, ambassador campaigns.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("brand_campaign_form"):
        brand_name = st.text_input("Brand name", "Nike")
        campaign_type = st.selectbox(
            "Campaign type",
            ["Run Club", "Padel Tournament", "Wellness Breakfast", "Gym Challenge", "Founder Sports Night"]
        )
        audience = st.multiselect(
            "Target audience",
            ["Russian-speaking expats", "Founders", "Premium fitness", "Women wellness", "Creators", "Investors"],
            default=["Russian-speaking expats", "Premium fitness"]
        )
        budget = st.slider("Campaign budget AED", 5000, 150000, 30000, 5000)

        if st.form_submit_button("Generate campaign concept", use_container_width=True, type="primary"):
            st.success(
                f"{brand_name} campaign: {campaign_type} for {', '.join(audience)}. "
                f"Indicative budget: AED {budget:,}. Suggested format: branded event + influencer content + community offer."
            )

elif page == "People":
    st.markdown("## People nearby")
    st.caption("This is where networking becomes visible and useful.")

    query = st.text_input("Search by role, sport, interest or location")
    people = PEOPLE
    if query:
        q = query.lower()
        people = [
            p for p in PEOPLE
            if q in p.name.lower()
            or q in p.role.lower()
            or q in p.location.lower()
            or any(q in s.lower() for s in p.sports)
            or any(q in i.lower() for i in p.interests)
        ]

    cols = st.columns(2)
    for i, person in enumerate(people):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card">
              <h3>{person.name}</h3>
              <p><b>{person.role}</b> · {person.location}</p>
              <p class="small-muted">{person.vibe}</p>
              <p>{", ".join(person.sports)}<br>{", ".join(person.interests)}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Connect", key=f"people_connect_{person.name}", use_container_width=True):
                if person.name not in st.session_state.connections:
                    st.session_state.connections.append(person.name)
                notify(f"Connection request sent to {person.name}")

elif page == "Map":
    st.markdown("## Live UAE social map")
    st.caption("Prototype map: visualizes density of people, circles and events.")

    st.markdown("""
    <div class="card"><h3>Dubai Marina</h3><p>🔥 3 events tonight · 12 people match your profile · Founder Padel active</p></div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card"><h3>Jumeirah</h3><p>🌿 Wellness Breakfast · Creator Run · brand activation opportunity</p></div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="card"><h3>Downtown Dubai</h3><p>🏙️ Business networking · social impact event · premium circles</p></div>
    """, unsafe_allow_html=True)

    if st.button("Find best area for me tonight", use_container_width=True, type="primary"):
        notify("Best area tonight: Dubai Marina — 94% fit with your profile")

elif page == "Profile":
    profile = st.session_state.profile
    st.markdown("## Your profile")
    st.markdown(f"""
    <div class="card">
      <h2>{profile["name"]} · {profile["location"]}</h2>
      <p>{profile["level"]} · {", ".join(profile["sports"])}</p>
      <p class="small-muted">Goals: {", ".join(profile["goals"])}</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Events", len(st.session_state.joined_events))
    with c2:
        metric_card("Connections", len(st.session_state.connections))
    with c3:
        metric_card("Intro requests", len(st.session_state.intro_requests))
    with c4:
        metric_card("Brand offers", len(st.session_state.saved_offers))

    st.write("")
    st.markdown("### Saved brand offers")
    if st.session_state.saved_offers:
        for offer in st.session_state.saved_offers:
            st.markdown(f"<span class='tag'>{offer}</span>", unsafe_allow_html=True)
    else:
        st.caption("No saved offers yet.")

    st.write("")
    st.markdown("""
    <div class="dark-card">
      <span class="premium-tag">Premium</span>
      <h2>Unlock high-signal circles</h2>
      <p>Invite-only communities, AI introductions, VIP events, brand perks and business networking.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Upgrade · 15 AED/month", use_container_width=True, type="primary"):
        st.session_state.profile["premium"] = True
        notify("Premium activated in prototype")

elif page == "Business":
    st.markdown("## Business model")
    st.caption("Partner and monetization dashboard for brands, gyms, venues and suppliers.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Subscription", "10–15 AED", "Monthly premium")
    with c2:
        metric_card("Commission", "5–10%", "Bookings and events")
    with c3:
        metric_card("Brand collabs", "High margin", "Sponsored activations")
    with c4:
        metric_card("Venues", "B2B", "Promoted listings")

    st.write("")
    st.markdown("### Sponsor-ready event builder")
    with st.form("sponsor_form"):
        brand = st.text_input("Brand name", "Premium Sportswear Brand")
        event_type = st.selectbox("Activation type", ["Creator Run", "Padel Tournament", "Wellness Breakfast", "Founder Sports Night"])
        budget = st.slider("Indicative sponsor budget AED", 5000, 100000, 25000, 5000)
        target = st.multiselect("Target audience", ["Founders", "Expats", "Women wellness", "Premium fitness", "Creators"], default=["Expats", "Premium fitness"])
        submit = st.form_submit_button("Generate activation concept", use_container_width=True, type="primary")
        if submit:
            st.success(f"{brand} concept: {event_type} for {', '.join(target)} with AED {budget:,} sponsor budget.")

elif page == "Admin":
    st.markdown("## Admin / Prototype database")
    st.caption("This page shows how the prototype state changes when buttons are clicked.")

    st.json({
        "profile": st.session_state.profile,
        "joined_events": st.session_state.joined_events,
        "joined_circles": st.session_state.joined_circles,
        "connections": st.session_state.connections,
        "intro_requests": st.session_state.intro_requests,
        "saved_offers": st.session_state.saved_offers,
        "brand_activations": st.session_state.brand_activations,
        "notifications": st.session_state.notifications[:10],
        "last_updated": datetime.now().isoformat()
    })

    if st.button("Reset prototype state", use_container_width=True):
        for key in ["joined_events", "joined_circles", "connections", "intro_requests", "saved_offers", "brand_activations"]:
            st.session_state[key] = []
        st.session_state.notifications = ["Prototype state reset."]
        st.rerun()