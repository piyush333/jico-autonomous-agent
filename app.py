import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load .env
env_file = '.env'
if os.path.exists(env_file):
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

from supabase import create_client

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    logger.error("Missing Supabase credentials!")
    exit(1)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

logger.info("🚀 JICO Agent Starting")
try:
    data = supabase.table('budget_status').select('*').limit(1).execute()
    logger.info("✅ Supabase connection verified!")
    logger.info("✅ Agent ready!")
except Exception as e:
    logger.error(f"❌ Error: {e}")
    exit(1)
