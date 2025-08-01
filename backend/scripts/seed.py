"""Seed data for development and testing."""

import logging
from datetime import UTC, datetime, timedelta

from sqlmodel import Session, select

from app.models import Membership, Project, User
from app.models.enums import UserRole
from app.services.auth import AuthService

logger = logging.getLogger(__name__)

users = [
    User(
        email="john.doe@example.com",
        username="johndoe",
        first_name="John",
        last_name="Doe",
        hashed_password=AuthService.get_password_hash("password_1"),
    ),
    User(
        first_name="Jane",
        last_name="Smith",
        username="janesmith",
        email="jane.smith@example.com",
        hashed_password=AuthService.get_password_hash("password_2"),
    ),
    User(
        first_name="Mike",
        last_name="Johnson",
        username="mikejohnson",
        email="mike.johnson@example.com",
        hashed_password=AuthService.get_password_hash("password_3"),
    ),
    User(
        first_name="Sarah",
        last_name="Wilson",
        username="sarahwilson",
        email="sarah.wilson@example.com",
        hashed_password=AuthService.get_password_hash("password_4"),
    ),
]

projects = [
    Project(
        name="E-commerce MMM Campaign",
        description="Marketing mix modeling for online retail campaign analysis",
        owner_id=users[0].id,
    ),
    Project(
        name="Brand Awareness Study",
        description="Multi-channel brand awareness attribution modeling",
        owner_id=users[1].id,
    ),
    Project(
        name="Holiday Campaign 2024",
        description="Q4 holiday season marketing effectiveness analysis",
        owner_id=users[0].id,
    ),
]

memberships = [
    Membership(
        project_id=projects[0].id,
        user_id=users[1].id,
        role=UserRole.VIEWER,
        invited_by=users[0].id,
        joined_at=datetime.now(UTC) - timedelta(days=20),
    ),
    Membership(
        project_id=projects[1].id,
        user_id=users[2].id,
        role=UserRole.EDITOR,
        invited_by=users[1].id,
        joined_at=datetime.now(UTC) - timedelta(days=5),
    ),
    Membership(
        project_id=projects[0].id,
        user_id=users[3].id,
        role=UserRole.VIEWER,
        invited_by=users[0].id,
        joined_at=datetime.now(UTC) - timedelta(days=1),
    ),
]


def create_sample_users(session: Session) -> list[User]:
    """Create sample users for development."""
    for user in users:
        # Check if user already exists
        existing = session.get(User, user.id)
        if not existing:
            session.add(user)

    session.commit()
    return users


def create_sample_projects(session: Session) -> list[Project]:
    """Create sample projects for development."""
    for project in projects:
        # Check if project already exists
        existing = session.get(Project, project.id)
        if not existing:
            session.add(project)

    session.commit()
    return projects


def create_sample_memberships(session: Session) -> list[Membership]:
    """Create sample memberships for development."""
    for membership in memberships:
        # Check if membership already exists
        existing = session.get(Membership, membership.id)
        if not existing:
            session.add(membership)

    session.commit()
    return memberships


# def create_sample_datasets(
#     session: Session,
#     created_projects: list[Project],
# ) -> list[Dataset]:
#     """Create sample datasets for development."""
#     # Create datasets using the actual project IDs from the database
#     sample_datasets = [
#         Dataset(
#             id="ds-001",
#             project_id=created_projects[0].id,
#             name="Q3 Media Performance Data",
#             file_url="https://example.com/datasets/q3-media-data.csv",
#             uploaded_at=datetime.now(UTC) - timedelta(days=5),
#             time="date",
#             kpi="conversions",
#             kpi_type=KpiType.REVENUE,
#             geo="region",
#             population="target_audience_size",
#             revenue_per_kpi="revenue_per_conversion",
#             controls=["seasonality", "promotions", "competitor_activity"],
#             medias=["facebook_ads", "google_ads", "tv_spots", "radio"],
#             media_spend=["facebook_spend", "google_spend", "tv_spend", "radio_spend"],
#             media_to_channel={
#                 "facebook_ads": "social_media",
#                 "google_ads": "search",
#                 "tv_spots": "traditional",
#                 "radio": "traditional",
#             },
#             media_spend_to_channel={
#                 "facebook_spend": "social_media",
#                 "google_spend": "search",
#                 "tv_spend": "traditional",
#                 "radio_spend": "traditional",
#             },
#         ),
#         Dataset(
#             id="ds-002",
#             project_id=created_projects[0].id,
#             name="Historical Sales Data",
#             file_url="https://example.com/datasets/historical-sales.csv",
#             uploaded_at=datetime.now(UTC) - timedelta(days=3),
#             time="week",
#             kpi="sales_volume",
#             kpi_type=KpiType.NON_REVENUE,
#             controls=["weather", "events"],
#             medias=["display_ads", "email_campaigns"],
#             media_spend=["display_budget", "email_budget"],
#             media_to_channel={
#                 "display_ads": "digital_display",
#                 "email_campaigns": "email",
#             },
#             media_spend_to_channel={
#                 "display_budget": "digital_display",
#                 "email_budget": "email",
#             },
#         ),
#         Dataset(
#             id="ds-003",
#             project_id=created_projects[1].id,
#             name="Brand Tracking Survey",
#             file_url="https://example.com/datasets/brand-tracking.csv",
#             uploaded_at=datetime.now(UTC) - timedelta(days=1),
#             time="month",
#             kpi="brand_awareness",
#             kpi_type=KpiType.NON_REVENUE,
#             controls=["market_conditions"],
#             medias=["youtube_ads", "instagram_ads", "podcast_ads"],
#             media_spend=["youtube_spend", "instagram_spend", "podcast_spend"],
#             media_to_channel={
#                 "youtube_ads": "video",
#                 "instagram_ads": "social_media",
#                 "podcast_ads": "audio",
#             },
#             media_spend_to_channel={
#                 "youtube_spend": "video",
#                 "instagram_spend": "social_media",
#                 "podcast_spend": "audio",
#             },
#         ),
#     ]

#     for dataset in sample_datasets:
#         # Check if dataset already exists
#         existing = session.get(Dataset, dataset.id)
#         if not existing:
#             session.add(dataset)

#     session.commit()
#     return sample_datasets


# def create_sample_pipelines(
#     session: Session,
#     created_projects: list[Project],
#     created_datasets: list[Dataset],
# ) -> list[Pipeline]:
#     """Create sample pipelines for development."""
#     # Create pipelines using the actual project and dataset IDs from the database
#     sample_pipelines = [
#         Pipeline(
#             id="pipe-001",
#             project_id=created_projects[0].id,
#             dataset_id=created_datasets[0].id,  # Q3 Media Performance Data
#             model_spec=ModelSpec(
#                 max_lag=7,
#                 hill_before_adstock=True,
#                 unique_sigma_for_each_geo=False,
#                 paid_media_prior_type=PaidMediaPrior.ROI,
#             ).model_dump(),
#         ),
#         Pipeline(
#             id="pipe-002",
#             project_id=created_projects[0].id,
#             dataset_id=created_datasets[1].id,  # Historical Sales Data
#             model_spec=ModelSpec(
#                 max_lag=10,
#                 hill_before_adstock=False,
#                 unique_sigma_for_each_geo=True,
#                 paid_media_prior_type=PaidMediaPrior.MROI,
#             ).model_dump(),
#         ),
#         Pipeline(
#             id="pipe-003",
#             project_id=created_projects[1].id,
#             dataset_id=created_datasets[2].id,  # Brand Tracking Survey
#             model_spec=ModelSpec(
#                 max_lag=5,
#                 hill_before_adstock=True,
#                 unique_sigma_for_each_geo=False,
#                 paid_media_prior_type=PaidMediaPrior.CUSTOM,
#             ).model_dump(),
#         ),
#     ]

#     for pipeline in sample_pipelines:
#         # Check if pipeline already exists
#         existing = session.get(Pipeline, pipeline.id)
#         if not existing:
#             session.add(pipeline)

#     session.commit()
#     return sample_pipelines


# def create_sample_jobs(
#     session: Session,
#     created_pipelines: list[Pipeline],
# ) -> list[Job]:
#     """Create sample jobs for development."""
#     sample_jobs = [
#         Job(
#             id="job-001",
#             pipeline_id=created_pipelines[0].id,
#             status=JobStatus.completed,
#             params=JobParams(
#                 prior=PriorParams(n_draws=1000),
#                 posterior=PosteriorParams(
#                     n_chains=4,
#                     n_adapt=1000,
#                     n_burnin=2000,
#                     n_keep=3000,
#                 ),
#             ).model_dump(),
#             started_at=datetime.now(UTC) - timedelta(hours=2),
#             finished_at=datetime.now(UTC) - timedelta(minutes=30),
#         ),
#         Job(
#             id="job-002",
#             pipeline_id=created_pipelines[1].id,
#             status=JobStatus.running,
#             params=JobParams(
#                 prior=PriorParams(n_draws=2000),
#                 posterior=PosteriorParams(
#                     n_chains=6,
#                     n_adapt=1500,
#                     n_burnin=3000,
#                     n_keep=5000,
#                 ),
#             ).model_dump(),
#             started_at=datetime.now(UTC) - timedelta(minutes=45),
#         ),
#         Job(
#             id="job-003",
#             pipeline_id=created_pipelines[2].id,
#             status=JobStatus.pending,
#             params=JobParams(
#                 prior=PriorParams(n_draws=500),
#                 posterior=PosteriorParams(
#                     n_chains=2,
#                     n_adapt=500,
#                     n_burnin=1000,
#                     n_keep=2000,
#                 ),
#             ).model_dump(),
#         ),
#         Job(
#             id="job-004",
#             pipeline_id=created_pipelines[0].id,
#             status=JobStatus.failed,
#             params=JobParams(
#                 prior=PriorParams(n_draws=800),
#                 posterior=PosteriorParams(
#                     n_chains=3,
#                     n_adapt=800,
#                     n_burnin=1500,
#                     n_keep=2500,
#                 ),
#             ).model_dump(),
#             started_at=datetime.now(UTC) - timedelta(days=1),
#             finished_at=datetime.now(UTC) - timedelta(days=1) + timedelta(minutes=15),
#             error="Insufficient data points for convergence",
#         ),
#     ]

#     for job in sample_jobs:
#         # Check if job already exists
#         existing = session.get(Job, job.id)
#         if not existing:
#             session.add(job)

#     session.commit()
#     return sample_jobs


# def create_sample_models(
#     session: Session,
#     created_jobs: list[Job],
# ) -> list[Model]:
#     """Create sample models for development."""
#     # Only create models for completed jobs
#     completed_jobs = [job for job in created_jobs if job.status == JobStatus.completed]

#     if not completed_jobs:
#         logger.info("No completed jobs found, skipping model creation")
#         return []

#     sample_models = [
#         Model(
#             id="model-001",
#             job_id=completed_jobs[0].id,  # Completed job
#             uri="https://storage.googleapis.com/meridian-models/model-001.pkl",
#             deployed=True,
#             created_at=datetime.now(UTC) - timedelta(minutes=25),
#         ),
#         Model(
#             id="model-002",
#             job_id=completed_jobs[
#                 0
#             ].id,  # Another model from same completed job (A/B test scenario)
#             uri="https://storage.googleapis.com/meridian-models/model-002.pkl",
#             deployed=False,
#             created_at=datetime.now(UTC) - timedelta(minutes=20),
#         ),
#     ]

#     for model in sample_models:
#         # Check if model already exists
#         existing = session.get(Model, model.id)
#         if not existing:
#             session.add(model)

#     session.commit()
#     return sample_models


# def create_sample_api_keys(
#     session: Session,
#     created_projects: list[Project],
# ) -> list[Key]:
#     """Create sample API keys for development."""
#     # Generate some sample API keys for different projects
#     sample_keys = []

#     sample_keys.extend(
#         [
#             Key(
#                 project_id=created_projects[0].id,
#                 description="Production API key for automated reporting",
#                 expires_at=datetime.now(UTC) + timedelta(days=90),
#                 is_active=True,
#                 created_at=datetime.now(UTC) - timedelta(days=30),
#                 updated_at=datetime.now(UTC) - timedelta(days=30),
#             ),
#             Key(
#                 project_id=created_projects[0].id,
#                 description="Development testing key",
#                 expires_at=datetime.now(UTC) + timedelta(days=30),
#                 is_active=True,
#                 created_at=datetime.now(UTC) - timedelta(days=15),
#                 updated_at=datetime.now(UTC) - timedelta(days=15),
#             ),
#             Key(
#                 project_id=created_projects[0].id,
#                 description="CI/CD pipeline integration",
#                 expires_at=datetime.now(UTC) + timedelta(days=60),
#                 is_active=True,
#                 created_at=datetime.now(UTC) - timedelta(days=7),
#                 updated_at=datetime.now(UTC) - timedelta(days=7),
#             ),
#             Key(
#                 project_id=created_projects[1].id,
#                 description="Brand tracking data collection",
#                 expires_at=datetime.now(UTC) + timedelta(days=120),
#                 is_active=True,
#                 created_at=datetime.now(UTC) - timedelta(days=20),
#                 updated_at=datetime.now(UTC) - timedelta(days=20),
#             ),
#             Key(
#                 project_id=created_projects[1].id,
#                 description="Expired test key (demonstration)",
#                 expires_at=datetime.now(UTC) - timedelta(days=5),  # Expired
#                 is_active=False,  # Deactivated
#                 created_at=datetime.now(UTC) - timedelta(days=45),
#                 updated_at=datetime.now(UTC) - timedelta(days=6),
#             ),
#             Key(
#                 project_id=created_projects[2].id,
#                 description="Holiday campaign analytics",
#                 expires_at=None,  # Never expires
#                 last_used_at=None,  # Never used yet
#                 is_active=True,
#                 created_at=datetime.now(UTC) - timedelta(days=3),
#                 updated_at=datetime.now(UTC) - timedelta(days=3),
#             ),
#         ],
#     )

#     for key in sample_keys:
#         # Check if key already exists
#         existing = session.get(Key, key.id)
#         if not existing:
#             session.add(key)

#     session.commit()

#     # Log the actual API keys for development purposes
#     logger.info("🔑 Generated API Keys (for development only):")
#     for key in sample_keys:
#         logger.info("  %s (%s...): %s", key.id, key.description[:30], key.key)

#     return sample_keys


def seed_database(session: Session) -> None:
    """Seed the database with sample data."""
    logger.info("🌱 Starting database seeding...")

    # Create users
    logger.info("👥 Creating sample users...")
    created_users = create_sample_users(session)
    logger.info("✅ Created %d users", len(created_users))

    # Create projects
    logger.info("📁 Creating sample projects...")
    created_projects = create_sample_projects(session)
    logger.info("✅ Created %d projects", len(created_projects))

    # Create memberships
    logger.info("👥 Creating sample memberships...")
    created_memberships = create_sample_memberships(session)
    logger.info("✅ Created %d memberships", len(created_memberships))

    # # Create datasets
    # logger.info("📊 Creating sample datasets...")
    # created_datasets = create_sample_datasets(session, created_projects)
    # logger.info("✅ Created %d datasets", len(created_datasets))

    # # Create pipelines
    # logger.info("🔗 Creating sample pipelines...")
    # created_pipelines = create_sample_pipelines(
    #     session, created_projects, created_datasets
    # )
    # logger.info("✅ Created %d pipelines", len(created_pipelines))

    # # Create jobs
    # logger.info("🚀 Creating sample jobs...")
    # created_jobs = create_sample_jobs(session, created_pipelines)
    # logger.info("✅ Created %d jobs", len(created_jobs))

    # # Create models
    # logger.info("📦 Creating sample models...")
    # created_models = create_sample_models(session, created_jobs)
    # logger.info("✅ Created %d models", len(created_models))

    # # Create API keys
    # logger.info("🔑 Creating sample API keys...")
    # created_keys = create_sample_api_keys(session, created_projects)
    # logger.info("✅ Created %d API keys", len(created_keys))

    logger.info("🎉 Database seeding completed!")


def clear_users(session: Session) -> None:
    """Clear all users from the database."""
    logger.info("🧹 Clearing users...")
    users = session.exec(select(User)).all()
    for user in users:
        session.delete(user)
    session.commit()
    logger.info("✅ Users cleared!")


def clear_projects(session: Session) -> None:
    """Clear all projects from the database."""
    logger.info("🧹 Clearing projects...")
    projects = session.exec(select(Project)).all()
    for project in projects:
        session.delete(project)
    session.commit()
    logger.info("✅ Projects cleared!")


def clear_memberships(session: Session) -> None:
    """Clear all memberships from the database."""
    logger.info("🧹 Clearing memberships...")
    memberships = session.exec(select(Membership)).all()
    for membership in memberships:
        session.delete(membership)
    session.commit()
    logger.info("✅ Memberships cleared!")


def clear_seed_data(session: Session) -> None:
    """Clear all seed data from the database."""
    logger.info("🧹 Clearing seed data...")
    clear_memberships(session)
    clear_projects(session)
    clear_users(session)
    session.commit()
    logger.info("✅ Seed data cleared!")


if __name__ == "__main__":
    from app.core.db import engine

    with Session(engine) as session:
        seed_database(session)
