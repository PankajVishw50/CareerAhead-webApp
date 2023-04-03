from app.model import User, Gender, CounsellorType
from app import db
import time


'''
    Item in counsellors:
    [ Username: string, email: string, password: string, image: string, age:integer, fee:integer, experience:integer, 
    description:string, role_id:integer, gender_id:integer, counsellor_type:integer ]
    
    To add more counsellors or edit existing ones modify this file.
'''
counsellors = [
    [
        "john doe",
        "john.doe@gmail.com",
        "john doe",
        "counsellor_john_doe.jpg",
        35,
        100,
        5,
        """
Hi, my name is John Doe and I'm a cognitive behavioral therapist. 
Over the last 5 years, I've had the privilege of working with a diverse group of clients and helping them overcome a variety of mental health challenges. 
I specialize in cognitive behavioral therapy, which is an evidence-based approach to treating a wide range of mental health disorders.

As a cognitive behavioral therapist, my approach focuses on helping clients identify and change negative thought patterns and behaviors that 
to their mental health problems. I work collaboratively with my clients to develop customized treatment plans that are tailored to their unique needs.
Through our work together, my goal is to help my clients develop the skills and tools they need to overcome their challenges and live a fulfilling life.

I believe that building a strong therapeutic relationship is key to achieving successful outcomes in therapy. 
That's why I take the time to get to know my clients and understand their struggles. I provide a safe and non-judgmental space where 
can feel comfortable sharing their thoughts and feelings.

In addition to my expertise in cognitive behavioral therapy, 
I also have experience working with clients from diverse backgrounds and with a range of mental health challenges.
I'm passionate about helping people overcome their challenges and I'm committed to staying up-to-date with the latest research and best 
practices in the field of counseling.

Overall, I feel privileged to work as a counselor and to have the opportunity to make a positive difference in the lives of my clients. 
If you're struggling with a mental health challenge, please don't hesitate to reach out to me. Together, we can work towards achieving your goals and
creating a brighter future. 
        """,
        2,
        2,
        1
    ],
    [
        "emily jones",
        "emily.jones@gmail.com",
        "emily jones",
        "counsellor_emily_jones.jpg",
        42,
        120,
        10,
        """
Hi there, I'm Jacob Lee, a male counselor specializing in addiction therapy. With 3 years of experience in the field, I have helped many individuals overcome addiction and regain control of their lives. Addiction is a complex and challenging issue, but with the right support and guidance, it is possible to break free from the cycle of substance abuse.

As an addiction therapist, I use evidence-based practices such as cognitive-behavioral therapy (CBT) and motivational interviewing to help clients identify the root causes of their addiction and develop healthy coping strategies. I believe in taking a holistic approach to addiction treatment, addressing not just the physical symptoms but also the emotional and psychological aspects of addiction.

In my work with clients, I create a safe, non-judgmental space where individuals can explore their feelings, beliefs, and behaviors without fear of stigma or shame. I believe that addiction is a disease, not a moral failing, and I work to help my clients understand and internalize this perspective.

In addition to my expertise in addiction therapy, I also have experience working with individuals struggling with trauma, anxiety, and depression. I believe that addiction often co-occurs with other mental health challenges, and I work to help my clients address these issues as well.

Overall, my goal as a counselor is to help individuals overcome addiction and achieve long-term recovery. I'm here to support you on your journey towards healing and growth, and I look forward to working with you.
        """,
        2,
        1,
        2
    ],
    [
        "jacob lee",
        "jacob.lee@gmail.com",
        "jacob lee",
        "counsellor_jacob_lee.jpg",
        28,
        80,
        3,
        """
Hello, my name is Sophia Patel and I'm a female counselor specializing in mental health therapy. With 15 years of experience in the field, I have helped many individuals overcome a wide range of mental health challenges and improve their overall well-being.

Mental health is a complex and multifaceted issue that affects people in different ways. As a mental health therapist, I use a variety of evidence-based practices such as cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT), and mindfulness-based interventions to help my clients address their specific needs and goals.

In my work with clients, I create a warm and empathetic space where individuals can explore their thoughts and feelings without judgment or pressure. I believe that everyone has the capacity for growth and change, and I work to help my clients tap into their inner strengths and resources to achieve their desired outcomes.

In addition to my expertise in mental health therapy, I also have experience working with individuals who have experienced trauma, grief and loss, and relationship issues. I believe that mental health challenges are often interconnected with other life experiences, and I work to help my clients understand and address these connections.

My ultimate goal as a counselor is to help my clients achieve greater self-awareness, resilience, and fulfillment in their lives. If you're struggling with mental health challenges or simply want to improve your overall well-being, I'm here to help. Let's work together to unlock your full potential and create the life you deserve.
        """,
        2,
        2,
        3
    ],
    [
        "sophia patel",
        "sophia.patel@gmail.com",
        "sophia patel",
        "counsellor_sophia_patel.jpg",
        50,
        150,
        15,
        """
Hello, I'm Aiden Kim and I'm a male counselor specializing in career counseling. With 8 years of experience in the field, I have helped individuals from all walks of life navigate the complexities of the modern job market and achieve their professional goals.

I understand that finding the right career path can be a daunting and overwhelming task. As a career counselor, I work with my clients to identify their unique strengths, skills, and values and help them explore potential career paths that align with their interests and aspirations.

Whether you're a recent graduate starting your career or an experienced professional looking to make a change, I offer a range of services to help you achieve success. From career assessments and skill-building exercises to job search strategies and interview preparation, I'm here to support you every step of the way.

In addition to my expertise in career counseling, I also have experience working with individuals dealing with workplace stress, burnout, and other job-related challenges. I believe that a fulfilling career is one of the cornerstones of a happy and fulfilling life, and I work to help my clients achieve both professional and personal success.

My approach to counseling is compassionate, empathetic, and results-oriented. I believe that with the right tools and support, anyone can achieve their career goals and find success in their chosen field. If you're looking for guidance and support in your career journey, I'm here to help. Let's work together to create a roadmap to your professional success.
        """,
        2,
        1,
        4
    ],
    [
        "aiden kim",
        "aiden.kim@gmail.com",
        "aiden kim",
        "counsellor_aiden_kim.jpg",
        38,
        110,
        8,
        """
Hi, my name is Samantha Nguyen and I am a female counselor specializing in genetic counseling. With 7 years of experience in the field, I am passionate about helping individuals and families navigate the complex world of genetics and make informed decisions about their health.

As a genetic counselor, I work with individuals who may be at risk for genetic conditions or who have already received a genetic diagnosis. I provide information about the condition, explain how it is inherited, and offer support as individuals and families make decisions about testing, treatment, and future planning.

I am committed to helping my clients understand their genetic information and empowering them to make informed decisions about their health. I offer a range of services including genetic testing, risk assessment, and genetic counseling for couples considering starting a family.

In addition to my work as a genetic counselor, I also have experience working with individuals dealing with grief, loss, and other life challenges. I believe that everyone has the capacity for resilience and growth, even in the face of difficult circumstances.

My approach to counseling is client-centered, compassionate, and non-judgmental. I believe that everyone has a unique story and perspective, and I work to create a safe and supportive space for my clients to share their experiences.

If you are facing a genetic health concern or need support navigating life's challenges, I am here to help. Let's work together to help you achieve the best possible outcomes for your health and well-being.

        """,
        2,
        2,
        5
    ],

    [
        "samantha nguyen",
        "samantha.nguyen@gmail.com",
        "samantha nguyen",
        "counsellor_samantha_nguyen.jpg",
        31,
        90,
        7,
        """
Hi, my name is Ashley Kim and I am a female counselor with a background in art therapy. I believe that art has the power to heal and transform individuals, and I am passionate about helping my clients use creative expression to work through emotional and psychological challenges.

As an art therapist, I work with individuals of all ages and backgrounds, using a variety of art materials and techniques to help my clients explore and express their inner experiences. I specialize in working with individuals dealing with trauma, anxiety, depression, and other mental health concerns.

My approach to counseling is grounded in empathy, non-judgment, and creativity. I believe that every person has the capacity for healing and growth, and I work to support my clients in tapping into their own innate resources to find solutions and create meaningful change in their lives.

If you are interested in exploring the healing power of art therapy, or if you are struggling with emotional or psychological challenges and are looking for a supportive and creative space to work through them, I am here to help. Let's work together to uncover your inner wisdom and strength and find a path forward that is grounded in healing and growth.
        """,
        2,
        1,
        7
    ],
    [
        "daniel rodriguez",
        "daniel.rodriguez@gmail.com",
        "daniel rodriguez",
        "counsellor_daniel_rodriguez.jpg",
        37,
        110,
        8,
        """
Hello, my name is Peter Chen and I am a male psychotherapist with 15 years of experience working with individuals dealing with a wide range of mental health concerns. I am committed to helping my clients find greater clarity, balance, and well-being in their lives.

As a psychotherapist, I work with individuals dealing with depression, anxiety, trauma, addiction, and other mental health challenges. I offer a variety of therapeutic approaches including cognitive-behavioral therapy, psychodynamic therapy, and mindfulness-based approaches, and I tailor my approach to each individual's unique needs and goals.

My goal is to provide a safe and supportive space where my clients feel seen, heard, and understood. I believe that the therapeutic relationship is a critical component of the healing process, and I work to build a collaborative and trusting relationship with each of my clients.

If you are struggling with mental health concerns and are looking for support and guidance, I am here to help. Let's work together to uncover the root causes of your challenges, develop coping strategies, and find greater balance and well-being in your life.
        """,
        2,
        2,
        5
    ],
    [
        "ashley kim",
        "ashley.kim@gmail.com",
        "ashley kim",
        "counsellor_ashley_kim.jpg",
        26,
        75,
        3,
        "i specialize in working with adolescents and young adults to navigate issues related to identity, relationships, and self-esteem.",
        2,
        1,
        12
    ],
    [
        "peter chen",
        "peter.chen@gmail.com",
        "peter chen",
        "counsellor_peter_chen.jpg",
        48,
        150,
        15,
        "as a career counselor, i work with individuals to explore career options, develop job search strategies, and prepare for interviews.",
        2,
        2,
        9
    ],
    [
        "natalie park",
        "natalie.park@gmail.com",
        "natalie park",
        "counsellor_natalie_park.jpg",
        33,
        100,
        6,
        "i am a licensed clinical social worker with experience providing individual and group therapy to adults with mood disorders and personality disorders.",
        2,
        1,
        4
    ],

    [
        "jackson lee",
        "jackson.lee@gmail.com",
        "jackson lee",
        "counsellor_jackson_lee.jpg",
        29,
        80,
        5,
        "i specialize in helping couples navigate relationship issues and develop communication and conflict resolution skills.",
        2,
        2,
        3
    ],
    [
        "grace yu",
        "grace.yu@gmail.com",
        "grace yu",
        "counsellor_grace_yu.jpg",
        42,
        120,
        10,
        "i am a licensed marriage and family therapist with experience helping families improve communication and resolve conflicts.",
        2,
        1,
        2
    ],
    [
        "stephanie jones",
        "stephanie.jones@gmail.com",
        "stephanie jones",
        "counsellor_stephanie_jones.jpg",
        35,
        95,
        6,
        "as a grief counselor, i help individuals process and cope with loss and grief, including the loss of loved ones, relationships, and opportunities.",
        2,
        1,
        8
    ],
    [
        "ryan kim",
        "ryan.kim@gmail.com",
        "ryan kim",
        "counsellor_ryan_kim.jpg",
        31,
        90,
        6,
        "i specialize in working with individuals who have experienced childhood trauma, including emotional, physical, and sexual abuse.",
        2,
        2,
        7
    ],
    [
        "kelly wong",
        "kelly.wong@gmail.com",
        "kelly wong",
        "counsellor_kelly_wong.jpg",
        27,
        70,
        3,
        "as a school counselor, i work with students to develop social and emotional skills, manage stress and anxiety, and plan for their futures.",
        2,
        1,
        11
    ],

    [
        "jessica li",
        "jessica.li@gmail.com",
        "jessica li",
        "counsellor_jessica_li.jpg",
        37,
        110,
        8,
        "as a career counselor, i help individuals identify their strengths and passions and develop a plan to achieve their professional goals.",
        2,
        1,
        5
    ],
    [
        "daniel chen",
        "daniel.chen@gmail.com",
        "daniel chen",
        "counsellor_daniel_chen.jpg",
        44,
        130,
        12,
        "i specialize in working with individuals who struggle with addiction and helping them develop strategies for recovery and relapse prevention.",
        2,
        2,
        14
    ],
    [
        "emily zhang",
        "emily.zhang@gmail.com",
        "emily zhang",
        "counsellor_emily_zhang.jpg",
        30,
        85,
        5,
        "as a mindfulness-based counselor, i help individuals develop self-awareness, manage stress and anxiety, and cultivate inner peace.",
        2,
        1,
        9
    ],
    [
        "alexander wu",
        "alexander.wu@gmail.com",
        "alexander wu",
        "counsellor_alexander_wu.jpg",
        39,
        115,
        10,
        "i specialize in helping individuals and couples improve their sex lives and overcome sexual dysfunction and performance anxiety.",
        2,
        2,
        4
    ],
    [
        "sophia cheng",
        "sophia.cheng@gmail.com",
        "sophia cheng",
        "counsellor_sophia_cheng.jpg",
        33,
        95,
        6,
        "as a trauma-informed counselor, i work with individuals who have experienced trauma to help them heal, build resilience, and reclaim their lives.",
        2,
        1,
        7
    ],

    [
        "kevin zhang",
        "kevin.zhang@gmail.com",
        "kevin zhang",
        "counsellor_kevin_zhang.jpg",
        28,
        80,
        4,
        "as a cognitive-behavioral therapist, i help individuals identify and change negative thought patterns and behaviors that contribute to mental health issues.",
        2,
        2,
        16
    ],
    [
        "hannah wu",
        "hannah.wu@gmail.com",
        "hannah wu",
        "counsellor_hannah_wu.jpg",
        31,
        90,
        6,
        "as a family therapist, i help families improve communication, resolve conflicts, and build stronger, more supportive relationships.",
        2,
        1,
        18
    ],
    [
        "isaac chen",
        "isaac.chen@gmail.com",
        "isaac chen",
        "counsellor_isaac_chen.jpg",
        40,
        120,
        11,
        "as a career counselor, i help individuals explore their passions and identify career paths that align with their values, interests, and skills.",
        2,
        2,
        5
    ],
    [
        "olivia huang",
        "olivia.huang@gmail.com",
        "olivia huang",
        "counsellor_olivia_huang.jpg",
        35,
        100,
        7,
        "as a grief counselor, i help individuals navigate the complex emotions and challenges of loss and find meaning and healing in the midst of pain.",
        2,
        1,
        11
    ],
    [
        "ethan liu",                       # username   0
        "ethan.liu@gmail.com",             # Email      1
        "ethan liu",                       # password   2
        "counsellor_ethan_liu.jpg",        # image      3
        45,                                # age        4
        140,                               # fee        5
        13,                                # experience 6
        "i specialize in helping individuals and couples build strong, healthy relationships and navigate the challenges of intimacy and commitment.",
        2,                                 # role id    8
        2,                                 # Gender id  9
        1                                  # Type of counsellor 10
    ]

]


# This function creates Counsellor types and add them to CounsellorType table in database
def create_type():
    counsellor_types = [
        'cognitive behavioral',
        'marriage and family',
        'addiction',
        'mental health',
        'career',
        'school',
        'genetic',
        'bereavement',
        'psychotherapist',
        'child',
        'rehabilitation',
        'art',
        'spiritual',
        'behavioral',
        'trauma',
        'anger management',
        'financial',
        'couples',
        'sex',
        'group'
    ]

    for type in counsellor_types:
        db.session.add(CounsellorType(type=type))

    db.session.commit()


# This function add counsellors to User table in database
def create_counsellors():

    for counsellor in counsellors:
        print("-------:: ", counsellor[0])

        usr = User(username=counsellor[0], email=counsellor[1], password=counsellor[2],
                   image=counsellor[3], age=counsellor[4], fee=counsellor[5],
                   experience=counsellor[6], description=counsellor[7],
                   role_id=counsellor[8], gender_id=counsellor[9])
        usr.type_of.append(CounsellorType.query.get(counsellor[10]))
        db.session.add(usr)
        time.sleep(.5)  # Added sleeper cause sqlite3 cannot handle continuous insertion of data
    db.session.commit()

    return "completed"


# This function add genders to Gender table in database
def create_gender():
    female = Gender(gender="female")    # 1
    male = Gender(gender="male")        # 2

    db.session.add_all([female, male])
    db.session.commit()