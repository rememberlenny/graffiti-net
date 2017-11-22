set :branch, ENV.fetch("CAPISTRANO_BRANCH", "development")
set :mb_sidekiq_concurrency, 1

server "staging.graffiti-net.org",
       :user => "deployer",
       :roles => %w[app backup cron db redis sidekiq web]
