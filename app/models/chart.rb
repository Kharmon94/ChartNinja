class Chart < ApplicationRecord
  belongs_to :user
  has_one_attached :image

  validates :title, presence: true, length: { minimum: 3, maximum: 100 }
  validates :description, length: { maximum: 500 }
  # validates :results, presence: true
  validate :image_type

  private

  def image_type
    if image.attached? && !image.content_type.in?(%w(image/jpeg image/png))
      errors.add(:image, 'must be a JPEG or PNG')
    elsif image.attached? == false
      errors.add(:image, 'required')
    end
  end
end
