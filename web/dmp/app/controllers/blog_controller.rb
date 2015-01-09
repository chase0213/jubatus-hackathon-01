class BlogController < ApplicationController
  def index
    @articles = Article.all
  end

  def search
    #ES使える?
    #@articles = Article.search
    search_word = params[:search_word]
    if search_word.blank?
      @articles = Article.all
    else
      @articles = Article.search(search_word)
    end
  end
end
