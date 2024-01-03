module ApplicationHelper
    def generate_image_url(attachment)
        if attachment.attached?
          Rails.logger.info "Generating URL for image."
          rails_blob_url(attachment, disposition: "attachment")
        else
          Rails.logger.warn "No attachment found to generate URL."
          nil
        end
    end
end
