class AdDeliverController < ApplicationController
  def fetchAds
    h_word = params[:text]
    if h_word.blank?
      render :json => false
      return
    end
    uri = URI.parse("http://10.0.1.91:80")
    Net::HTTP::start(uri.host, uri.port) do |http|
      request = Net::HTTP::Post.new(uri.path)
      request.set_form_data(h_word)
      response = http.request(request)
      render :json => response
    end
  end
end
