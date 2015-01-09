class Article < ActiveRecord::Base
  class << self 
    def search(search_word)
      Article.where("content like ?", "%" + search_word + "%")
    end
  end
end
