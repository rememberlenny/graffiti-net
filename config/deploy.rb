set :application, "graffiti-net"
set :repo_url, "https://github.com/rememberlenny/graffiti-net.git"

# Project-specific overrides go here.
# For list of variables that can be customized, see:
# https://github.com/mattbrictson/capistrano-mb/blob/master/lib/capistrano/tasks/defaults.rake

fetch(:mb_recipes) << "sidekiq"
fetch(:mb_aptitude_packages)["redis-server@ppa:chris-lea/redis-server"] = :redis

set :mb_dotenv_keys, %w[
  rails_secret_key_base
  postmark_api_key
  redis_url
  sidekiq_web_username
  sidekiq_web_password
]

after "deploy:published", "bundler:clean"
