<script>
    const developers = [
        {
            name: "Purusottam Gajurel",
            role: "Student",
            bio: "THA078BCT032",
            image: "developer1.jpg",
            email: "purusottam@example.com",
        },
        {
            name: "Sagar Bikram Adhikari",
            role: "Student",
            bio: "THA078BCT037",
            image: "developer2.jpg",
            email: "sagar@example.com",
        },
        {
            name: "Sameer Shrestha",
            role: "Student",
            bio: "THA078BCT038",
            image: "developer3.jpg",
            email: "sameer@example.com",
        },
    ];
</script>

<style>
    /* General Styles */
    .container {
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 40px 0;
    }

    h1 {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 40px;
    }

    /* Team Grid */
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 40px;
    }

    .team-card {
        background: #fff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .team-card:hover {
        transform: translateY(-10px);
    }

    .team-img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        margin-bottom: 15px;
        object-fit: cover;
    }

    .team-card h3 {
        font-size: 1.5rem;
        margin-bottom: 5px;
    }

    .role {
        font-size: 1rem;
        color: #777;
        margin-bottom: 10px;
    }

    .bio {
        font-size: 0.9rem;
        color: #555;
        margin-bottom: 15px;
    }

    .contact-link {
        display: inline-block;
        padding: 8px 16px;
        background: #007BFF;
        color: #fff;
        border-radius: 5px;
        text-decoration: none;
        font-size: 0.9rem;
        transition: background 0.3s ease;
    }

    .contact-link:hover {
        background: #0056b3;
    }

    /* Additional Information */
    .additional-info {
        background: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    .additional-info h2 {
        font-size: 1.8rem;
        margin-bottom: 10px;
    }

    .additional-info p {
        font-size: 1rem;
        color: #555;
        margin-bottom: 20px;
    }

    .additional-info a {
        color: #007BFF;
        text-decoration: none;
    }

    .additional-info a:hover {
        text-decoration: underline;
    }
</style>

<!-- About Section -->
<section class="about-section">
    <div class="container">
        <h1>About Us</h1>
        <p class="subtitle">Meet the team behind this blog platform.</p>

        <!-- Developer Cards -->
        <div class="team-grid">
            {#each developers as developer}
                <div class="team-card">
                    <img src={developer.image} alt={developer.name} class="team-img" />
                    <h3>{developer.name}</h3>
                    <p class="role">{developer.role}</p>
                    <p class="bio">{developer.bio}</p>
                    <a href={`mailto:${developer.email}`} class="contact-link">Contact</a>
                </div>
            {/each}
        </div>

        <!-- Additional Information -->
        <div class="additional-info">
            <h2>Our Mission</h2>
            <p>We aim to provide a seamless blogging experience for writers and readers alike, powered by cutting-edge technology.</p>
            <h2>Contact Us</h2>
            <p>For inquiries, reach out to us at <a href="mailto:info@concept.com">info@concept.com</a>.</p>
        </div>
    </div>
</section>