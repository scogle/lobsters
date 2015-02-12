class << Rails.application
	def domain
	  "ontonews.com"
	end

	def name
	  "OntoNews"
	end
end

Rails.application.routes.default_url_options[:host] = Rails.application.domain