class ClinicianReviewGenerator:

    def generate(self, state):

        review_items = []

        if state.requires_review:

            if (
                "Missing"
                in state.demographics["name"]
            ):
                review_items.append(
                    "Patient name missing"
                )

            if (
                "Missing"
                in state.demographics["age"]
            ):
                review_items.append(
                    "Patient age missing"
                )

            if (
                "Missing"
                in state.demographics["gender"]
            ):
                review_items.append(
                    "Patient gender missing"
                )

            review_items.extend(
                state.pending_results
            )

            review_items.extend(
                state.conflicts
            )

            review_items.extend(
                state.warnings
            )

        return review_items